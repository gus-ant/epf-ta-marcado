from bottle import request, template #usado pra acessar dados de formularios HTTP
from models.user import UserModel, User
from exceptions import EmailAlreadyUsedException
from models.events import EventModel
from services.event_service import EventService
from exceptions import EmailAlreadyUsedException, PasswordMismatchException
from utils.id_tracker import get_next_id 

class UserService:
    # Esta classe atua como uma camada intermediária entre o controlador (rotas)
    # E o modelo de dados, implementando a lógica de negócio.: 

    def __init__(self):
        self.user_model = UserModel() # acessa o usermodel de user.py
        self.event_model = EventModel()
        self.event_service = EventService() 


    def get_all(self):
        users = self.user_model.get_all() #usa o metodo de user.py
        return users


    def save(self):
        new_id = get_next_id('user_id') #agora usa um metodo novo que garante que mesmo apagando user, o id vai ser sempre o mais atualizado
        name = request.forms.get('name') #pega esse dado diretamente do formulario http
        email = request.forms.get('email')
        birthdate = request.forms.get('birthdate')
        password = request.forms.get('password') #puxa a senha do formulario
        password_confirm = request.forms.get('password_confirm') #serve pra confirmar a senha
        if password != password_confirm:
            session = request.environ.get('beaker.session')
            raise PasswordMismatchException()

            #Agora o Exception é utilizado corretamente
        adm = request.forms.get('adm') == 'on' #é um checkbox, on se marcado, none se não 
        
        if not password: #verifica se não foi colocada uma senha 
            raise ValueError("É obrigatorio ter uma senha")
        #como no tpl diz que é obrigatorio, depois tentar tirar aqui
        
        if self.user_model.get_by_email(email): #verifica se o email ja existe
            raise EmailAlreadyUsedException(email)

        user = User(id=new_id, name=name, email=email, birthdate=birthdate, password=password, adm=adm) #cria o objeto de user
        self.user_model.add_user(user) #adiciona na memoria



    def get_by_id(self, user_id):
        return self.user_model.get_by_id(user_id) #usa o metodo de user.py
    
    def get_by_email(self, email):
        self.user_model.users = self.user_model._load() #atualiza
        return self.user_model.get_by_email(email) #usa o metodo de user.py


    def edit_user(self, user): #usa um objeto user
        name = request.forms.get('name') #puxa os dados do formulario http
        email = request.forms.get('email') #ISSO AQUI PODE DAR UM PROBLEMÃO
        birthdate = request.forms.get('birthdate')
        password = request.forms.get('password')
        password_confirm = request.forms.get('password_confirm')

        if password or password_confirm:
            if password != password_confirm:
                return template('user_form', error='as senhas digitadas não coincidem', user = user, action = f"/users/edit/{user.id}")

        existing_user = self.user_model.get_by_email(email) #verifica um user que já tem o mesmo email
        if existing_user and existing_user.id != user.id: #caso o email seja usado por outro user, raiser error
            raise EmailAlreadyUsedException(email)
        
        user.name = name #sobrescreve os dados
        user.email = email
        user.birthdate = birthdate

        if password and password.strip(): #só troca de senha caso uma nova for fornecida
            user.set_password(password)

        self.user_model.update_user(user) #usa o metodo do user.py


    def delete_user(self, user_id):
        user = self.user_model.get_by_id(user_id)
        if user: #caso encontre
            if user.adm: #se for adm
                eventos = [e for e in self.event_service.get_all() if e.owner_email == user.email] #lista com todos os eventos do adm
                for e in eventos:
                    self.event_service.delete_event(e.id) #apaga o evento
            self.event_service.remove_user_from_all_events(user.email) #tira o user de todos os eventos
            self.user_model.delete_user(user_id) #usa o metodo do user.py (já salva)

    def authenticate(self, email, password):
        #autentica um usuario usando email e senha
        user = self.user_model.get_by_email(email)
        if user and user.check_password(password): #caso a senha for correta
            return user
        return None #caso for incorreta
    
    def get_admins(self): #retorna apenas os admins
        return self.user_model.get_admins()
    
    def get_regular_users(self): #retorna apenas usuarios comuns
        return self.user_model.get_regular_users()
    
    def can_create_events(self, user): #verifica se o usuario pode criar eventos
        return user and user.adm
    
    def get_events_user_participates(self, user_email: str):
        self.event_model.events = self.event_model._load()
        return [e for e in self.event_model.events if user_email in e.participants_emails] #lista de todos os eventos que tem um participante com o mesmo email
    
    def get_events_by_owner(self, owner_email: str):
        self.event_model.events = self.event_model._load()
        return [e for e in self.event_model.events if owner_email == e.owner_email] #lista de todos os eventos que um adm tem
    
    def verify_password(self, email, input_password):
        user = self.get_by_email(email)
        if not user:
            return False
        return input_password == user.password


