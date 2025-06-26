from bottle import Bottle, request, redirect
from .base_controller import BaseController
from services.event_service import EventService
from utils.decorators import login_required, admin_required
from services.payment_service import PaymentService

class EventController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.event_service = EventService()
        self.payment_service = PaymentService()  
        self.setup_routes()
        
    
    def setup_routes(self):
        self.app.route('/events', method='GET', callback=self.list_events)
        self.app.route('/events/create', method=['GET', 'POST'], callback=self.create_event)
        self.app.route('/events/<event_id:int>/join', method='POST', callback=self.join_event)
        self.app.route('/events/<event_id:int>', method='GET', callback=self.view_event)

    def list_events(self):
        eventos = self.event_service.get_all()
        return self.render('events', eventos=eventos)
    
    @login_required
    def join_event(self, event_id):
        session = request.environ['beaker.session']
        email = session['user']   

        event = self.event_service.get_by_id(event_id)
        if not event:
            return "Evento não encontrado", 404

        # cria pagamento pendente
        payment = self.payment_service.create_payment(
            event_id=event.id,
            user_email=email,
            amount=event.price
        )
        
        print(f"AQUI ESTÁ: {payment.event_id}" )

        return redirect(f'/payments/{int(payment.id)}')



    def payment_page(self, payment_id):
        payment = self.payment_service.get_by_id(int(payment_id))
        if not payment:
            return "Pagamento não encontrado man", 404

        if request.method == 'POST':
            
            self.payment_service.mark_as_paid(payment_id)
            # atualiza capacidade do evento
            self.event_service.decrease_capacity(payment.event_id)
            return self.render('payment_success', payment=payment)

        return redirect('payment_form', payment=payment)

    
    # esse python decorator serve apenas para que só usuários adms logados consigam acessar
    @admin_required
    def create_event(self):
        session = request.environ['beaker.session'] #puxa o user logado
        email = session.get('user')
        if request.method == 'GET':
            return redirect('event_form', action='/events/create', error = None)
        else:
            try:
                name = request.forms.get('name')
                local = request.forms.get('local')
                date = request.forms.get('date')  # formato obrigatório yyyy-mm-dd
                time = request.forms.get('time')  # formato obrigatorio hh:mm
                price = 0 
                if request.forms.get('price'): #só coloca preço caso tenha
                    price = float(request.forms.get('price'))
                max_capacity = int(request.forms.get('max_capacity'))
                owner_email = email #agora puxa automatico
                description = request.forms.get('description')

                self.event_service.add_event(name, local, date, time, price, max_capacity, owner_email, description)

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

