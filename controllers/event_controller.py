from bottle import Bottle, request, redirect
from .base_controller import BaseController
from services.event_service import EventService
from services.user_service import UserService
from services.payment_service import PaymentService
from utils.decorators import login_required, admin_required
from services.payment_service import PaymentService
import os, uuid

UPLOAD_DIR = './static/uploads/event_covers' #local onde as capas de eventos são salvas

class EventController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.event_service = EventService()
        self.payment_service = PaymentService()  
        self.user_service = UserService()
        self.setup_routes()
        
    
    def setup_routes(self):
        self.app.route('/events', method='GET', callback=self.list_events)
        self.app.route('/events/create', method=['GET', 'POST'], callback=self.create_event)
        self.app.route('/events/<event_id:int>/join', method='POST', callback=self.join_event)
        self.app.route('/events/<event_id:int>', method='GET', callback=self.view_event)
        self.app.route('/events/<event_id:int>/leave', method='POST', callback=self.exit_event)
        self.app.route('/events/search', method='GET', callback=self.search_event)

    def list_events(self):
        session = request.environ.get('beaker.session')
        user = None
        if session and 'user' in session:
            email = session['user']['email']
            user = self.user_service.get_by_email(email)

        events = self.event_service.get_all()
        return self.render('events', events=events, user=user)
    
    #join event será modificado:
    #agora só cria o pagamento, para entrar no evento, deve confirmar o pagamento (payment_controller)
    @login_required
    def join_event(self, event_id):
        session = request.environ['beaker.session']
        email = session['user']['email']

        event = self.event_service.get_by_id(event_id)
        if not event:
            return "Evento não encontrado", 404
        
        if email in self.event_service.get_participants(event.id):
            return "Já participa do evento"

        if event.price >0:
            payment = self.payment_service.create_payment(
                event_id=event.id,
                user_email=email,
                amount=event.price
            )
            return redirect(f'/payments/{int(payment.id)}')
        payment = self.payment_service.create_payment(
            event_id=event.id,
            user_email=email,
            amount=0
        )
        return redirect(f'/payments/{int(payment.id)}')

    #o exit event é usado quando o user sai do evento
    #quando o user pede reembolso o metodo usado tá em payment_controller
    @login_required
    def exit_event(self, event_id): 
        session = request.environ['beaker.session']
        email = session['user']['email']

        event = self.event_service.get_by_id(event_id)
        if not event:
            return "Evento não encontrado", 404
        
        if email not in event.participants_emails:
            return "Você não participa desse evento"
        
        self.event_service.remove_participant(event_id, email) #tira ele do evento

        last_payment = self.payment_service.get_by_event_participant(event_id, email)
        if last_payment:
            pid = last_payment.id

            if last_payment.status == 'pending': #caso pending, marcar cancelled
                self.payment_service.mark_as_cancelled(pid)
            elif event.price == 0:#caso de graça marcar refunded
                self.payment_service.mark_as_refunded(pid) 
            elif last_payment.status == 'paid':
                self.payment_service.mark_as_refund_requested(pid) #buscar pagamento, caso fosse paid, marcar refund_requested

        return redirect(f'/user')

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
        email = session['user']['email']
        if request.method == 'GET':
            return self.render('event_form', action='/events/create', event=None, error=None)
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
                cover_file = request.files.get('cover')

                filename = None #trata dos casos onde não tem imagem enviada

                if cover_file and cover_file.filename: #puxa o filename do arquivo enviado
                    tipo = os.path.splitext(cover_file.filename)[1] #tipo do arquivo
                    nome_unico = uuid.uuid4().hex #cria um novo nome unico, pra tratar dos casos onde existem 2 imagens de mesmo nome
                    filename = f"{nome_unico}{tipo}" 
                    save_path = os.path.join(UPLOAD_DIR, filename) #local onde vai ser salvo
                    os.makedirs(os.path.dirname(save_path), exist_ok=True) #cria o dir caso não exista
                    cover_file.save(save_path) #guarda a imagem
                    

                self.event_service.add_event(name, local, date, time, price, max_capacity, owner_email, description, cover=filename)

                return self.redirect('/user')
            except Exception as e:
                

                return self.render('event_form', action='/events/create', event=None, error=str(e))

            
    def view_event(self, event_id):
        session = request.environ.get('beaker.session')
        user = None
        if session and 'user' in session:
            email = session['user']['email']
            user = self.user_service.get_by_email(email)
        event = self.event_service.get_by_id(event_id)
        if not event:
            return "Evento não encontrado"
        return self.render('event_detail', event=event, user=user)

    def search_event(self):
        pesquisa = request.query.get("q", "").lower()

        # para buscar todos os eventos
        eventos = self.event_service.get_all()

        eventos_filtrados = [
            e for e in eventos
            if pesquisa in str(e.name).lower() or
               pesquisa in str(e.local).lower() or
               pesquisa in str(e.description).lower()
        ]
        
        return self.render('event_search', events=eventos_filtrados, query=pesquisa)


event_routes = Bottle()
event_controller = EventController(event_routes)

