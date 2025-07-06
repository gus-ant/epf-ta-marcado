# Usar mais as Exceptions

class BaseException(Exception): #Excessão base
    def __init__(self, mensagem, detalhes=None):
        super().__init__(mensagem)
        self.detalhes = detalhes

class EmailAlreadyUsedException(BaseException):
    #Erro caso um usuario do sistema já tenha esse email
    mensagem = "Este email já está sendo usado por outro usuario"

    def __init__(self, email=None):
        if email:
            self.mensagem = f"O email '{email}' já está sendo usado por outro usuario"

        super().__init__(self.mensagem)
        self.email = email

class PasswordMismatchException(BaseException):
    def __init__(self):
        super().__init__("As senhas digitadas não coincidem")

class PaymentNotFoundException(BaseException):
    def __init__(self):
        super().__init__("O pagamento não foi encontrado")



        