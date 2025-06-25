import json, os, datetime
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

class Payment:
    def __init__(self, id, event_id, user_email, amount, status='pending', timestamp=None):
        self.id = int(id)
        self.event_id = event_id
        self.user_email = user_email
        self.amount = amount
        self.status = status          
        self.timestamp  = timestamp

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, d):
        d['id'] = int(d['id']) 
        d['event_id'] = int(d['event_id']) 
        d['amount'] = float(d['amount'])  
        return cls(**d)


class PaymentModel:
    FILE_PATH = os.path.join(DATA_DIR, 'payments.json')

    def __init__(self):
        self.payments = self._load()

    def _load(self):
        if not os.path.exists(self.FILE_PATH): return []
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            txt = f.read().strip()
            if not txt: return []
            return [Payment.from_dict(x) for x in json.loads(txt)]

    def _save(self):
        os.makedirs(os.path.dirname(self.FILE_PATH), exist_ok=True)
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([p.to_dict() for p in self.payments], f, indent=4, ensure_ascii=False)


    def add(self, payment):
        self.payments.append(payment)
        self._save()

    def get_by_id(self, pid):
        self._load()
        print(f"[DEBUG] Procurando pagamento com ID: {pid}")
        print(f"[DEBUG] IDs disponíveis: {[p.id for p in self.payments]}")
        return next((p for p in self.payments if p.id == pid), None)

    def update(self, payment):
        for i, p in enumerate(self.payments):
            if p.id == payment.id:
                self.payments[i] = payment
                self._save()
                break
