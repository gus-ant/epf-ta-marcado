import json, os, datetime
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

class Payment:
    def __init__(self, id, event_id, user_id, amount, event_name, status='pending', timestamp=None):
        self.id = int(id)
        self.event_id = event_id
        self.user_id = user_id
        self.amount = amount
        self.event_name = event_name or ''
        self.status = status          
        self.timestamp  = timestamp or datetime.datetime.now().isoformat()
        

    def to_dict(self):
        return {
            'id': self.id,
            'event_id': self.event_id,
            'user_id': self.user_id,
            'amount': self.amount,
            'event_name': self.event_name,
            'status': self.status,
            'timestamp': self.timestamp
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id = data['id'],
            event_id = data['event_id'],
            user_id = data['user_id'],
            amount = data['amount'],
            event_name = data.get('event_name', ''),
            status = data['status'],
            timestamp = data['timestamp']
        )


class PaymentModel:
    FILE_PATH = os.path.join(DATA_DIR, 'payments.json')

    def __init__(self):
        self.payments = self._load()

    def _load(self):
        if not os.path.exists(self.FILE_PATH): return []

        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            txt = f.read().strip()
            if not txt or txt == '': return []

            data=json.loads(txt)
            return [Payment.from_dict(x) for x in data]

    def _save(self):
        os.makedirs(os.path.dirname(self.FILE_PATH), exist_ok=True)
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([p.to_dict() for p in self.payments], f, indent=4, ensure_ascii=False)


    def add(self, payment):
        self.payments.append(payment)
        self._save()
        self.payments = self._load() #atualiza

    def get_by_id(self, pid):
        self.payments = self._load() #atualiza
        return next((p for p in self.payments if p.id == pid), None)
        #ta puxand o pagamento antigo
    
    def get_by_event_participant(self, event_id, user_id):
        self.payments = self._load() #atualiza
        return next((p for p in self.payments if p.event_id == event_id and p.user_id == user_id and (p.status != 'cancelled' and p.status != 'refunded')), None)
        #vai pegar um pagamento com mesmo email, event_id E que não esteja cancelado nem reembolsado
        #serve pra quando um user sair de um evento, poder pedir reembolso

    def get_all_from_user(self, user_id):
        self.payments = self._load() #atualiza
        return [p for p in self.payments if p.user_id == user_id]
        #devolve uma lista com todos os pagamentos do user

    def update(self, payment):
        self.payments = self._load()
        for i, p in enumerate(self.payments):
            if p.id == payment.id:
                self.payments[i] = payment
                self._save()
                self.payments = self._load()
                return True
        return False
