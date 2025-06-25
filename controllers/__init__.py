from bottle import Bottle
from controllers.user_controller import user_routes
from controllers.event_controller import event_routes
from controllers.auth_controller import auth_routes
from controllers.payment_controler import payment_routes

def init_controllers(app: Bottle):
    app.merge(user_routes)
    app.merge(event_routes)
    app.merge(auth_routes)
    app.merge(payment_routes)  
    # app.merge() é um método do Bottle que combina rotas de diferentes instâncias
    # Pega todas as rotas definidas em user_routes e adiciona à aplicação principal (app)
    # 
    # O que acontece internamente:
    # 1. user_routes contém rotas como: /users, /users/add, /users/edit, etc.
    # 2. merge() copia todas essas rotas para a aplicação principal
    # 3. Agora app tem acesso a todas as rotas de usuários
    #
    # Exemplo prático:
    # Antes: app só tem rotas básicas
    # Depois: app tem rotas básicas + todas as rotas de user_routes