from bottle import request, redirect, Bottle
from services.user_service import UserService
from controllers.base_controller import BaseController

class AuthController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.user_service = UserService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/login', method=['GET', 'POST'], callback=self.login)
        
        self.app.route('/logout', method='GET', callback=self.logout)

    def login(self):
        if request.method == 'POST':
            email = request.forms.get('email')
            password = request.forms.get('password')
            user = self.user_service.authenticate(email, password)
            if user:
                request.environ['beaker.session']['user'] = user.email
                redirect('/')
            else:
                return self.render('login', error='Login inválido')
        return self.render('login', error=None)

    def logout(self):
        session = request.environ['beaker.session']
        session.delete()
        redirect('/')

auth_routes = Bottle()
auth_controller = AuthController(auth_routes)
