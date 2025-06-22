from bottle import Bottle, request
from .base_controller import BaseController
import json
from services.event_service import EventService


class EventController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.event_service = EventService()
        self.setup_routes()
        
    def setup_routes(self):
        self.app.route('/events', method='GET', callback=self.list_events)
        self.app.route('/events/create', method=['GET', 'POST'], callback=self.create_event)
        self.app.route('/events/<event_id:int>', method='GET', callback=self.view_event)

    def list_events(self):

        eventos = self.event_service.get_all()
        return self.render('events', eventos=eventos)
    
    def create_event(self):
        if request.method == 'GET':
            return self.render('event_form', action='/events/create', error = None)
        else:
            try:
                name = request.forms.get('name')
                local = request.forms.get('local')
                date = request.forms.get('date')  # formato obrigatório yyyy-mm-dd
                time = request.forms.get('time')  # formato obrigatorio hh:mm
                price = float(request.forms.get('price'))
                max_capacity = int(request.forms.get('max_capacity'))

                owner_email = request.get_cookie('user_email') or 'anon@anon.com' 

                self.event_service.add_event(name, local, date, time, price, max_capacity, owner_email)

                return self.redirect('/events')
            except Exception as e:
                return self.render('event_form', action='/events/create', error=str(e))
            
    def view_event(self, event_id):
        evento = self.event_service.get_by_id(event_id)
        if not evento:
            return "Evento não encontrado"
        return self.render('event_detail', evento=evento)


event_routes = Bottle()
event_controller = EventController(event_routes)

