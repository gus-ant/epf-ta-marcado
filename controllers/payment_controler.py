from bottle import Bottle, redirect, HTTPError
from .base_controller import BaseController
from services.payment_service import PaymentService
from utils.decorators import login_required, admin_required
# ATENCAO: AINDA TEM UM CERTO DELAY QUANDO O USER CLICA NO CORACAO E ACESSA A PÁGINA DE PAYMENTS/<NUMBER>

class PaymentController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.payment_service = PaymentService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/<payment_id:int>', method='GET', callback=self.show_payment)
        self.app.route('/<payment_id:int>/confirm', method='POST', callback=self.confirm_payment)


    @login_required
    def show_payment(self, payment_id):
        print("Ate aqui DA SIM")
        pid = int(payment_id)
        
        print(pid)
        payment = self.payment_service.get_by_id(pid)
        print(payment)
        if not payment:
            # 404 padrão do Bottle
            return HTTPError(404, "Pagamento não encontrado.")
        # sucesso
        return self.render('payment_detail', payment=payment)


    def confirm_payment(self, payment_id):
        if self.payment_service.mark_as_paid(payment_id):
            return redirect(f'/payments/{payment_id}')   # volta a tela de detalhes do pagamento
        return "Erro ao confirmar pagamento"

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
            "tipo_ingresso": payment.ticket_type,  # você precisa armazenar esse campo
            "quantidade": payment.quantity,
            "valor_total": payment.amount
        }

        conteudo_qr = f"{dados_qr['evento']} | {dados_qr['data']} às {dados_qr['hora']} | {dados_qr['local']} | {dados_qr['tipo_ingresso']} | Qtd: {dados_qr['quantidade']} | R$ {dados_qr['valor_total']:.2f}"

        qr_base64 = gerar_qrcode_base64(conteudo_qr)


        return

payment_routes = Bottle()
payment_controler = PaymentController(payment_routes)