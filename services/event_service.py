from bottle import request #usado pra acessar dados de formularios HTTP
from models.events import EventModel, Event

class EventService:
    # Esta classe atua como uma camada intermediaria entre o controller (rotas)
    #e o modelo de dados, implementando a logica de negocio

    def __init__(self):
        self.event_model = EventModel()

    def get_all(self):
        events = self.event_model.get_all()
        return events
    
    def get_by_id(self, event_id):
        return self.event_model.get_by_id(event_id)
    
    def get_by_owner_email(self, event_owner_email):
        return self.event_model.get_by_owner_email(event_owner_email)
    
    def get_by_name(self, event_name):
        return self.event_model.get_by_name(event_name)
    
    def get_closed_events(self):
        return self.event_model.get_closed_events()
    
    def get_open_events(self):
        return self.event_model.get_open_events
    
    def save(self):
        last_id = max([e.id for e in self.event_model.get_all()], default=0) #busca o id mais alto ja usado pelo sistema
        new_id = last_id+1
        name = request.forms.get('name')
        owner_email = 'falta aqui' #puxar a pessoa que ta fazendo e usar email dela
        local = request.forms.get('local')
        date = request.forms.get('date')
        price = request.forms.get('price')
        max_capacity = request.forms.get('max_capacity')
        time = request.forms.get('time')

        event = Event(id=new_id, name=name, local=local, date=date, price=price, max_capacity=max_capacity, time=time, current_capacity=max_capacity, owner_email=owner_email)
        self.event_model.add_event(event)

    