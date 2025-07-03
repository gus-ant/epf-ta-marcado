from bottle import request
from models.payment import PaymentModel, Payment
from models.events import EventModel
from services.event_service import EventService

class PaymentService:
    def __init__(self):
        self.payment_model = PaymentModel()
        self.event_model = EventModel()
        self.event_service = EventService()

    def create_payment(self, event_id, user_email, amount):
        old_id = int(max([p.id for p in self.payment_model.payments], default=0))
        new_id = old_id+1
        event = self.event_model.get_by_id(event_id)
        event_name = event.name
        if amount >0:
            payment = Payment(new_id, event_id, user_email, amount, event_name)
        else:
            payment = Payment(new_id, event_id, user_email, 0, event_name, 'paid')

            #AQUI O USER ENTRA NO EVENTO
            event_id = payment.event_id
            session = request.environ.get('beaker.session')
            email = session['user']['email']
            self.event_service.add_participant(event_id, email) 

        self.payment_model.add(payment)
        return payment
    
    def add(self, payment):
        self.payment_model.add(payment) #agora sim

    def get_by_id(self, pid):
        return self.payment_model.get_by_id(pid)
    
    def get_by_event_participant(self, event_id, user_email):
        return self.payment_model.get_by_event_participant(event_id, user_email)
    
    def get_all_from_user(self, user_email):
        return self.payment_model.get_all_from_user(user_email)
    
    def get_all(self):
        payments = self.payment_model._load()
        return payments

    def mark_as_paid(self, pid):
        payment = self.get_by_id(pid)
        if payment:
            payment.status = 'paid'
            self.payment_model.update(payment)
            return True
        return False
    
    def mark_as_refund_requested(self, pid): 
        payment = self.get_by_id(pid)
        if payment:
            payment.status = 'refund_requested'
            self.payment_model.update(payment)
            if payment.amount == 0: #quando é de graça
                payment.status = 'refunded'
                self.payment_model.update(payment)
            return True
        return False
    
    def mark_as_refunded(self, pid):
        payment = self.get_by_id(pid)
        if payment:
            payment.status = 'refunded'
            self.payment_model.update(payment)
            return True
        return False
    
    def mark_as_cancelled(self, pid):
        payment = self.get_by_id(pid)
        if payment:
            payment.status = 'cancelled'
            self.payment_model.update(payment)
            return True
        return False
