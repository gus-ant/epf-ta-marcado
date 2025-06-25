from bottle import Bottle, redirect, HTTPError
from .base_controller import BaseController
from services.payment_service import PaymentService

# ATENCAO: AINDA TEM UM CERTO DELAY QUANDO O USER CLICA NO CORACAO E ACESSA A PÁGINA DE PAYMENTS/<NUMBER>

class PaymentController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.payment_service = PaymentService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/payments/<payment_id:int>', method='GET', callback=self.show_payment)
        self.app.route('/payments/<payment_id:int>/confirm', method='POST', callback=self.confirm_payment)


    def show_payment(self, payment_id):

        try:
            pid = int(payment_id)
        except ValueError:
            # ID inválido na URL → 400 Bad Request
            return HTTPError(400, "Payment ID inválido.")

        payment = self.payment_service.get_by_id(pid)

        if not payment:
            # 404 padrão do Bottle
            return HTTPError(404, "Pagamento não encontrado mano.")

        # sucesso
        return self.render('payment_detail', payment=payment)


    def confirm_payment(self, payment_id):
        if self.payment_service.mark_as_paid(payment_id):
            return redirect(f'/payments/{payment_id}')   # volta a tela de detalhes do pagamento
        return "Erro ao confirmar pagamento"

payment_routes = Bottle()
payment_controler = PaymentController(payment_routes)