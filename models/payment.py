import json, os, datetime
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

class Payment:
    def __init__(self, id, event_id, user_email, amount, status='pending', timestamp=None):
        self.id = int(id)
        self.event_id = event_id
        self.user_email = user_email
        self.amount = amount
        self.status = status          
        self.timestamp  = timestamp or datetime.datetime.now().isoformat()

    def to_dict(self):
        return {
            'id': self.id,
            'event_id': self.event_id,
            'user_email': self.user_email,
            'amount': self.amount,
            'status': self.status,
            'timestamp': self.timestamp
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id = data['id'],
            event_id = data['event_id'],
            user_email = data['user_email'],
            amount = data['amount'],
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
        self.payments = self._load()

    def get_by_id(self, pid):
        self.payments = self._load()
        print(f"[DEBUG] Procurando pagamento com ID: {pid}")
        print(f"[DEBUG] IDs disponíveis: {[p.id for p in self.payments]}")
        return next((p for p in self.payments if p.id == pid), None)

    def update(self, payment):
        for i, p in enumerate(self.payments):
            if p.id == payment.id:
                self.payments[i] = payment
                self._save()
                return True
        return False
