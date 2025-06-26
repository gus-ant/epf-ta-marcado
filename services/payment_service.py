from models.payment import PaymentModel, Payment

class PaymentService:
    def __init__(self):
        self.model = PaymentModel()

    def create_payment(self, event_id, user_email, amount):
        new_id = int(max([p.id for p in self.model.payments], default=0))
        payment = Payment(new_id+1, event_id, user_email, amount)
        self.model.add(payment)
        return payment
    
    def add(self, payment):
        self.payments.append(payment)
        self._save()  # já salva no arquivo JSON aqui

    def get_by_id(self, pid):
        self.model = PaymentModel()
        return self.model.get_by_id(pid)

    def mark_as_paid(self, pid):
        payment = self.get_by_id(pid)
        if payment:
            payment.status = 'paid'
            self.model.update(payment)
            return True
        return False
