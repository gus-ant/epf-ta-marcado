from models.payment import PaymentModel, Payment


class PaymentService:
    def __init__(self):
        self.payment_model = PaymentModel()
        

    def create_payment(self, event_id, user_email, amount): #rever isso aqui
        old_id = int(max([p.id for p in self.payment_model.payments], default=0))
        new_id = old_id+1
        payment = Payment(new_id, event_id, user_email, amount)
        self.payment_model.add(payment)
        return payment
    
    def add(self, payment):
        self.payment_model.add(payment) #agora sim

    def get_by_id(self, pid):
        return self.payment_model.get_by_id(pid)
    
    def get_payment_by_event_id(self, event_id):
        from services.event_service import EventService
        event_service = EventService()
        return event_service.get_by_id(event_id)

    def mark_as_paid(self, pid):
        payment = self.get_by_id(pid)
        if payment:
            payment.status = 'paid'
            self.payment_model.update(payment)
            return True
        return False
