from bottle import request #usado pra acessar dados de formularios HTTP
from models.events import EventModel, Event
from models.user import UserModel

class EventService:
    # Esta classe atua como uma camada intermediaria entre o controller (rotas)
    # e o modelo de dados, implementando a logica de negocio

    def __init__(self):
        self.event_model = EventModel()
        self.user_model = UserModel()
        self.event_model._load() #atualiza o sistema quando criar um evento novo

    def get_all(self):
        self.event_model._load()
        events = self.event_model.get_all()
        return events
    
    def get_by_id(self, event_id):
        self.event_model._load()
        return self.event_model.get_by_id(event_id)
    
    def get_by_owner_email(self, event_owner_email):
        self.event_model._load()
        return self.event_model.get_by_owner_email(event_owner_email)
    
    def get_by_name(self, event_name):
        self.event_model._load()
        return self.event_model.get_by_name(event_name)
    
    def get_closed_events(self):
        self.event_model._load()
        return self.event_model.get_closed_events()
    
    def get_open_events(self):
        self.event_model._load()
        return self.event_model.get_open_events()
    
    def add_event(self, name, local, date, time, price, max_capacity, owner_email, description='', cover=None, ):
        # gera um novo ID automaticamente com base nos eventos já existentes
        events = self.event_model.get_all()
        new_id = max([e.id for e in events], default=0) + 1

        event = Event(
            id=new_id,
            name=name,
            local=local,
            date=date,
            price=price,
            time=time,
            max_capacity=max_capacity,
            owner_email=owner_email,
            current_capacity=max_capacity,
            description=description,
            cover = cover
        )

        self.event_model.add_event(event)
        self.event_model.events = self.event_model._load()

    def delete_event(self, event_id):
        self.event_model.delete_event(event_id)
    
    def save(self):
        last_id = max([e.id for e in self.event_model.get_all()], default=0) #busca o id mais alto ja usado pelo sistema
        new_id = last_id+1
        name = request.forms.get('name')
        session = request.environ.get('beaker.session')
        owner_email = session['user']['email']
        local = request.forms.get('local')
        date = request.forms.get('date')
        price = request.forms.get('price')
        max_capacity = request.forms.get('max_capacity')
        time = request.forms.get('time')
        description = request.forms.get('description')

        event = Event(id=new_id, name=name, local=local, date=date, price=price, max_capacity=max_capacity, time=time, current_capacity=max_capacity, owner_email=owner_email, description=description)
        self.event_model.add_event(event)
        self.event_model.events = self.event_model._load()

    # a ideia é diminuir a capacidade do evento quando um user se inscrever
    def decrease_capacity(self, event_id):
        event = self.get_by_id(event_id)
        if event and event.current_capacity > 0:
            event.current_capacity -= 1
            self.event_model.update_event(event) 

    def increase_capacity(self, event_id):
        event = self.get_by_id(event_id)
        if event and event.current_capacity < event.max_capacity:
            event.current_capacity +=1
            self.event_model.update_event(event)


    def add_participant(self, event_id: int, user_email: str):
        event = self.get_by_id(event_id) #busca o evento
        if event and user_email not in event.participants_emails: #se o user não estiver no evento
            event.participants_emails.append(user_email) #coloca o email dele na lista de participantes
            self.decrease_capacity(event_id) #diminui as vagas
            self.event_model.update_event(event) #atualiza no sistema
    
    def remove_participant(self, event_id:int, user_email: str):
        event = self.get_by_id(event_id)
        if event and user_email in event.participants_emails:
            event.participants_emails.remove(user_email)
            self.increase_capacity(event_id)
            self.event_model.update_event(event)

    def remove_user_from_all_events(self, user_email: str): #util pra quando apagar o user
        events = self.event_model.get_all()
        for event in events: #para cada evento
            if user_email in event.participants_emails: #se o cabra estiver
                self.remove_participant(event.id, user_email) #tira ele

    def get_participants(self, event_id:int):
        return self.event_model.get_participants(event_id)     
        #retorna uma lista com todos os users que estiverem no evento

    