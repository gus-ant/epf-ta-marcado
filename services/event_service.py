from bottle import request #usado pra acessar dados de formularios HTTP
from models.events import EventModel, Event
from models.user import UserModel
from utils.id_tracker import get_next_id

class EventService:
    # Esta classe atua como uma camada intermediaria entre o controller (rotas)
    # e o modelo de dados, implementando a logica de negocio

    def __init__(self):
        self.event_model = EventModel()
        self.user_model = UserModel()
        self.event_model._load() #atualiza o sistema quando criar um evento novo

    def get_all(self):
        self.event_model.events = self.event_model._load()
        events = self.event_model.get_all()
        return events
    
    def get_by_id(self, event_id):
        self.event_model.events = self.event_model._load()
        return self.event_model.get_by_id(event_id)
    
    def get_by_owner_id(self, event_owner_id):
        self.event_model._load()
        return self.event_model.get_by_owner_id(event_owner_id)
    
    def get_by_name(self, event_name):
        self.event_model._load()
        return self.event_model.get_by_name(event_name)
    
    def get_closed_events(self):
        self.event_model._load()
        return self.event_model.get_closed_events()
    
    def get_open_events(self):
        self.event_model._load()
        return self.event_model.get_open_events()
    
    def add_event(self, name, local, date, time, price, max_capacity, owner_id, description='', cover=None, ):
        # gera um novo ID automaticamente com base nos eventos já existentes (correto mesmo caso um evento seja apagado)
        new_id = get_next_id('event_id')

        event = Event(
            id=new_id,
            name=name,
            local=local,
            date=date,
            price=price,
            time=time,
            max_capacity=max_capacity,
            owner_id=owner_id,
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
        owner_id = session['user']['id']
        local = request.forms.get('local')
        date = request.forms.get('date')
        price = request.forms.get('price')
        max_capacity = int(request.forms.get('max_capacity'))
        time = request.forms.get('time')
        description = request.forms.get('description')

        event = Event(id=new_id, name=name, local=local, date=date, price=price, max_capacity=max_capacity, time=time, owner_id=owner_id, description=description)
        self.event_model.add_event(event)
        self.event_model.events = self.event_model._load()



    def add_participant(self, event_id: int, user_id:int):
        print('entrou no evento')
        event = self.get_by_id(event_id) #busca o evento
        if event and (user_id not in event.participants_ids): #se o user não estiver no evento
            event.participants_ids.append(user_id) #coloca o id dele na lista de participantes
            self.event_model.update_event(event) #atualiza no sistema
    
    def remove_participant(self, event_id:int, user_id:int):
        event = self.get_by_id(event_id)
        if event and user_id in event.participants_ids:
            event.participants_ids.remove(user_id)
            print("removeu")
            self.event_model.update_event(event)
            #falta marcar no pagamento que saiu do evento, 'refund_requested'
            #quando reembolsado 'refunded'
            #adicionar a opção de cancelar pagamento, cancelled

    def remove_user_from_all_events(self, user_id:int):
        self.event_model.events = self.event_model._load()
        print(f"Removendo user_id: {user_id} de eventos...")
        for event in self.event_model.events:
            print(f"Evento {event.id} participantes: {event.participants_ids}")
            if event.participants_ids and user_id in event.participants_ids:
                event.participants_ids.remove(user_id)
                print(f'id removido do evento {event.id}')
        self.event_model._save()

    def get_participants(self, event_id:int):
        return self.event_model.get_participants(event_id)     
        #retorna uma lista com todos os users que estiverem no evento

    def get_participants_number(self, event_id:int):
        return self.event_model.get_participants_number(event_id)
    
    def get_15_next_events(self):
        return self.event_model.get_15_next_events()
    
    def get_future_events(self):
        return self.event_model.get_future_events()
    
    def get_past_events(self):
        return self.event_model.get_past_events()
    
    def get_top_15_events(self):
        return self.event_model.get_top_15_events()
    

    