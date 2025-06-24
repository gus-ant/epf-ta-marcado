from bottle import Bottle, run
from config import Config
from beaker.middleware import SessionMiddleware

class App:
    def __init__(self):
        self.bottle = Bottle()
        self.config = Config()


    def setup_routes(self):
        from controllers import init_controllers

        print('🚀 Inicializa rotas!')
        init_controllers(self.bottle)


    def run(self):
        self.setup_routes()

        #config do beaker (coisa que faz o login/logout)
        session_ops = {
        'session.type': 'cookie',
        'session.cookie_expires': True,
        'session.auto': True,
        'session.secret': Config.SECRET_KEY,
        'session.validate_key': Config.SECRET_KEY
        }

        app_with_session = SessionMiddleware(self.bottle, session_ops)

        run(
            app = app_with_session,
            host=self.config.HOST,
            port=self.config.PORT,
            debug=self.config.DEBUG,
            reloader=self.config.RELOADER
        )


def create_app():
    return App()
