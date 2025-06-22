from .base_controller import BaseController
from services import event_service
from bottle import Bottle, request

class HomeController(BaseController): # Também herda de basecontroler

    def __init__(self, app):
        super().__init__(app) #chama o construtor da classe pai

        self.setup_routes()
        self.event_service = EventService()
        self.setup_routes()


    def setup_routes():
        self.app.route('/', method='GET', callback=self.index)
