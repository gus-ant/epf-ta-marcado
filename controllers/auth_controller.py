from bottle import request, redirect, Bottle
from services.user_service import UserService
from controllers.base_controller import BaseController


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
        if request.method == 'POST':
            email = request.forms.get('email')
            password = request.forms.get('password')
            user = self.user_service.authenticate(email, password)
            if user: #conseguiu fazer o login
                session['user'] = user.email #PODE ACESSAR O EMAIL DE QUALQUER LUGAR
                session.save()
                redirect('/')
            else: #não acertou o login
                return self.render('login', error='Login inválido')
        return self.render('login', error=None)

    def logout(self):
        session = request.environ['beaker.session']
        session.delete()
        redirect('/login')

auth_routes = Bottle()
auth_controller = AuthController(auth_routes)

