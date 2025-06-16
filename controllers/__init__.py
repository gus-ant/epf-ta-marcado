from bottle import Bottle
from controllers.user_controller import user_routes

def init_controllers(app: Bottle):
    app.merge(user_routes)
