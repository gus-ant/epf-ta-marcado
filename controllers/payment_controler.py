from bottle import Bottle, redirect, request, HTTPError
from .base_controller import BaseController
from services.payment_service import PaymentService
from services.event_service import EventService
from utils.decorators import login_required
from utils.qr_code import gerar_qrcode_base64
from io import BytesIO
import base64
import qrcode
from io import BytesIO
from exceptions import PaymentNotFoundException

class PaymentController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.payment_service = PaymentService()
        self.event_service = EventService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/<payment_id:int>', method='GET', callback=self.show_payment)
        self.app.route('/<payment_id:int>/confirm', method='POST', callback=self.confirm_payment)
        self.app.route('/<payment_id:int>/cancel', method='POST', callback=self.cancel_payment)
        self.app.route('/<payment_id:int>/request_refund', method='POST', callback=self.request_refund)
        self.app.route('/<payment_id:int>/confirm_refund', method='POST', callback=self.confirm_refund)
        self.app.route('/payments/<payment_id:int>/qrcode', method='GET', callback=self.show_qr_code)



    @login_required
    def show_payment(self, payment_id):
        
        pid = int(payment_id)
        
        
        payment = self.payment_service.get_by_id(pid)

        if not payment:
            # adição do método raise paymentexception
            raise PaymentNotFoundException()
        
        payment = self.payment_service.get_by_event_participant(payment.event_id,payment.user_email)
        if payment == None:
            payment = self.payment_service.get_by_id(pid)

        if payment.amount == None:
            payment.amount = 0

        ticket_data = {
                "evento": f"{payment.event_id}",
                "usuario": payment.user_email,
                "valor": f"R$ {payment.amount:.2f}",
                "status": payment.status,
                "data": payment.timestamp
            }
        
        img = qrcode.make(ticket_data)
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        qr_code_base64 = base64.b64encode(buffer.getvalue()).decode()

        return self.render('payment_detail', payment=payment, qr_code=qr_code_base64)
    
    def cancel_payment(self, payment_id):
        if self.payment_service.mark_as_cancelled(payment_id):
            payment = self.payment_service.get_by_id(payment_id)
                # gera o QR Code com dados do ingresso

            if payment.amount == None:
                payment.amount = 0

            ticket_data = {
                "evento": f"{payment.event_id}",
                "usuario": payment.user_email,
                "valor": f"R$ {payment.amount:.2f}",
                "status": payment.status,
                "data": payment.timestamp
            }

            qr = qrcode.make(str(ticket_data))
            buffer = BytesIO()
            qr.save(buffer, format="PNG")
            qr_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
            qr_url = f"data:image/png;base64,{qr_base64}"
            
            # renderiza a tela com QR Code embutido
            return self.render('payment_success', payment=payment, qr_code=qr_url)

        return "Erro ao cancelar pagamento"
    
    def request_refund(self, payment_id):
        if self.payment_service.mark_as_refund_requested(payment_id):
            payment = self.payment_service.get_by_id(payment_id)
                # gera o QR Code com dados do ingresso
            ticket_data = {
                "evento": f"{payment.event_id}",
                "usuario": payment.user_email,
                "valor": f"R$ {payment.amount:.2f}",
                "status": payment.status,
                "data": payment.timestamp
            }

            qr = qrcode.make(str(ticket_data))
            buffer = BytesIO()
            qr.save(buffer, format="PNG")
            qr_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
            qr_url = f"data:image/png;base64,{qr_base64}"
            
            #AQUI O USER SAI DO EVENTO
            event_id = payment.event_id
            session = request.environ.get('beaker.session')
            email = session['user']['email']
            self.event_service.remove_participant(event_id, email)

            # renderiza a tela com QR Code embutido
            return self.render('payment_success', payment=payment, qr_code=qr_url)

        return "Erro ao pedir reembolso"
    
    def confirm_refund(self, payment_id):
        if self.payment_service.mark_as_refunded(payment_id):
            payment = self.payment_service.get_by_id(payment_id)
                # gera o QR Code com dados do ingresso
            ticket_data = {
                "evento": f"{payment.event_id}",
                "usuario": payment.user_email,
                "valor": f"R$ {payment.amount:.2f}",
                "status": payment.status,
                "data": payment.timestamp
            }

            qr = qrcode.make(str(ticket_data))
            buffer = BytesIO()
            qr.save(buffer, format="PNG")
            qr_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
            qr_url = f"data:image/png;base64,{qr_base64}"
            
            # renderiza a tela com QR Code embutido
            return self.render('payment_success', payment=payment, qr_code=qr_url)

        return "Erro ao confirmar reembolso"

    def confirm_payment(self, payment_id): 
        if self.payment_service.mark_as_paid(payment_id):
            payment = self.payment_service.get_by_id(payment_id)
            
            # gera o QR Code com dados do ingresso

            if payment.amount == None:
                payment.amount = 0

            ticket_data = {
                "evento": f"{payment.event_id}",
                "usuario": payment.user_email,
                "valor": f"R$ {payment.amount:.2f}",
                "status": payment.status,
                "data": payment.timestamp
            }

            qr = qrcode.make(str(ticket_data))
            buffer = BytesIO()
            qr.save(buffer, format="PNG")
            qr_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
            qr_url = f"data:image/png;base64,{qr_base64}"

            #AQUI O USER ENTRA NO EVENTO
            event_id = payment.event_id
            session = request.environ.get('beaker.session')
            email = session['user']['email']
            self.event_service.add_participant(event_id, email) 

            # renderiza a tela com QR Code embutido
            return self.render('payment_success', payment=payment, qr_code=qr_url)

        return "Erro ao confirmar pagamento"
    # esse método é simples até, mas precisa da biblioteca qrcode e pillow para funcionar
    def show_qr_code(self, payment_id):
        payment = self.payment_service.get_by_id(payment_id)
        if not payment or payment.status != 'paid':
            return "QR Code indisponível. O pagamento precisa estar confirmado.", 400
        event = self.event_service.get_by_id(payment.event_id)
        dados_qr = {
            "evento": event.name,
            "data": event.date,
            "hora": event.time,
            "local": event.local,
            #"tipo_ingresso": payment.ticket_type,  #  precisa armazenar (modificar payments) para armazenar esse campo
            #"quantidade": payment.quantity,  # add se necessário (sugestão)
            "valor_total": payment.amount
        }

        conteudo_qr = f"{dados_qr['evento']} | {dados_qr['data']} às {dados_qr['hora']} | {dados_qr['local']} | {dados_qr['tipo_ingresso']} | Qtd: {dados_qr['quantidade']} | R$ {dados_qr['valor_total']:.2f}"

        qr_base64 = gerar_qrcode_base64(conteudo_qr)
        return self.render('ticket.tpl', qr=qr_base64, dados=dados_qr)


payment_routes = Bottle()
payment_controler = PaymentController(payment_routes)