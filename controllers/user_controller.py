from bottle import Bottle, request
from .base_controller import BaseController
from services.user_service import UserService
from utils.decorators import login_required
from services.event_service import EventService
from services.payment_service import PaymentService
from exceptions import EmailAlreadyUsedException, PasswordMismatchException


class UserController(BaseController): #herda de BaseController

    def __init__(self, app):
        super().__init__(app) #chama o construtor da classe pai

        self.setup_routes()
        self.user_service = UserService()
        self.event_service = EventService()
        self.payment_service = PaymentService()


    
    def setup_routes(self): # Rotas User
        self.app.route('/user', method='GET', callback=self.view_profile) #registra a pagina de detalhes do user
        self.app.route('/users', method='GET', callback=self.list_users) #Registra rota GET /users que chama o método list_users para listar usuários
        self.app.route('/users/add', method=['GET', 'POST'], callback=self.add_user) #Registra rota /users/add que aceita GET (mostrar formulário) e POST (salvar usuário)
        self.app.route('/users/edit/<user_id:int>', method=['GET', 'POST'], callback=self.edit_user) #Registra rota /users/edit/<user_id> com parâmetro inteiro para editar usuário específico
        self.app.route('/users/delete/<user_id:int>', method=['GET', 'POST'], callback=self.confirm_delete_user) #Registra rota POST /users/delete/<user_id> para deletar usuário específico
        self.app.route('/user/payments', method='GET', callback=self.view_payments)


    def list_users(self):
        users = self.user_service.get_all() #users é a lista de todos os users
        return self.render('users', users=users) #renderiza o template users passando a lista de usuarios


    def add_user(self):
        if request.method == 'GET':
            session = request.environ.get('beaker.session')
            return self.render('user_form', user=None, action="/users/add", error=None, session=session)
        else:
            try:
                # salva o usuário e obtém o objeto
                user = self.user_service.save()

                if not user:
                    return self.render('user_form', user=None, action='/users/add', error="Erro ao criar usuário.", session=request.environ.get('beaker.session'))

                # vai autenticar o usuário automaticamente (mesmo processo que no login)
                session = request.environ.get('beaker.session')
                session['user'] = {
                    'email': user.email,
                    'name': user.name,
                    'adm': user.adm,
                    'id': user.id
                }
                session.save()

                print(f"USER {user.name} LOGADO AUTOMATICAMENTE")
                return self.redirect('/user')  # Redireciona para o perfil

            except (ValueError, EmailAlreadyUsedException, PasswordMismatchException) as e:
                session = request.environ.get('beaker.session')
                return self.render('user_form', user=None, action='/users/add', error=str(e), session=session)

            
    @login_required
    def view_profile(self):
        session = request.environ.get('beaker.session') #pega a sessao atual
        email = session['user']['email'] #pega o email
        user = self.user_service.get_by_email(email) #puxa o user
        if user:
            from services.event_service import EventService
            from services.payment_service import PaymentService

            payment_service = PaymentService()
            user_payments = payment_service.get_all()  # ou crie um método como get_by_user_id(user.id)

            # Filtro apenas dos pagamentos desse user
            # user_payments = [p for p in user_payments if p.user_email == user.email and p.status == "paid"]
            user_payments = [p for p in user_payments if p.user_email == user.email]

            # Eventos que o usuário participa ou criou
            if not user.adm:
                events = self.user_service.get_events_user_participates(email)
            else:
                events = self.user_service.get_events_by_owner(email)

            # Adiciona o ID do pagamento ao evento (para usar no botão)
            for event in events:
                matching_payment = next((p for p in user_payments if p.event_id == event.id), None)
                event.payment_id = matching_payment.id if matching_payment else None

            return self.render('user', user=user, events=events)
        return "user not found"
    
    @login_required
    def view_payments(self):
        session = request.environ.get('beaker.session')
        email = session['user']['email']
        user = self.user_service.get_by_email(email)
        payments = self.payment_service.get_all_from_user(email)

        return self.render('payments', user=user, payments=payments[::-1]) #envia a lista ao contrario pra facilitar visualização 


    def edit_user(self, user_id): #serve pra editar um usuario existente, usa o id
        user = self.user_service.get_by_id(user_id) #busca pelo id
        if not user:
            return "Usuário não encontrado" #retorna isso caso não exista esse usuario

        if request.method == 'GET':
            return self.render('user_form', user=user, action=f"/users/edit/{user_id}", error=None)
        else:
            # POST - salvar edição
            try:
                result = self.user_service.edit_user(user)
                if result: #trata dos erros
                    return result
                self.redirect('/user')
            except ValueError as e:
                return self.render('user_form', user=user, action=f"/users/edit/{user_id}", error=None)

    @login_required
    def delete_user(self, user_id):
        session = request.environ.get('beaker.session')

        self.user_service.delete_user(user_id) #remove o user

        if session.get('user') and session['user']['id'] == user_id:
            session.delete() #desloga da sessao
            session.save()

        self.redirect('/events') #redireciona 
    
    # @route('/user/delete', method=['GET', 'POST'])
    @login_required
    def confirm_delete_user(self, user_id):
        print("Método HTTP:", request.method)
        session = request.environ.get('beaker.session')
        user_id = session['user']['id']
        print('user id:', user_id)
        user = self.user_service.get_by_id(user_id)
        if not user:
            return "Usuário não encontrado", 404
        
        if request.method == 'GET':
            return self.render('confirm_delete_user', user=user, error=None)
        
        #POST
        senha_informada = request.forms.get('password')
        if not self.user_service.verify_password(user.email, senha_informada):
            return self.render('confirm_delete_user', user=user, error="Senha incorreta.")
        
        self.user_service.delete_user(user_id)
        session.delete()
        session.save()
        return self.redirect('/events')



user_routes = Bottle()
user_controller = UserController(user_routes)
