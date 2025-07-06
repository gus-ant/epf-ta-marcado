from bottle import request, redirect, Bottle
from services.user_service import UserService
from controllers.base_controller import BaseController
from utils.decorators import login_required
from models.user import User


# esse arquivo vai controlar a autenticação do Site, ainda não está pronto. 
# falta colocar o beaker em prática, que é uma biblioteca para controlar se o usuário está logado e quais requisições HTTPs ele pode fazer
# FLASK >>>> BOTTLE PQ O FLASK TEM SUPORTE A SEÇOES E AUTENTICAÇÃO

class AuthController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.user_service = UserService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/login', method=['GET', 'POST'], callback=self.login)
        self.app.route('/logout', method='GET', callback=self.logout)

    def login(self):
        session = request.environ['beaker.session']
        error = request.query.get('error') or ''

        if request.method == 'POST':
            email = request.forms.get('email')
            password = request.forms.get('password')

            user = self.user_service.authenticate(email, password)
            if user: #conseguiu fazer o login
                session['user'] = {
                    'email':user.email, #PODE ACESSAR O EMAIL DE QUALQUER LUGAR
                    'name':user.name, #agora o nome tambem pode ser acessado
                    'adm':user.adm, #agora dá pra ver se é adm
                    'id':user.id #id do user
                    }
                session.save()
                print(f"USER {user.name} LOGADO")
                
                redirect('/')
            else: #não acertou o login
                return self.render('login', error='Login inválido')
        return self.render('login', error=error)

    @login_required      
    def logout(self):
        session = request.environ['beaker.session']
        print(f"USER DESLOGADO")
        session.delete()
        redirect('/login')

auth_routes = Bottle()
auth_controller = AuthController(auth_routes)

