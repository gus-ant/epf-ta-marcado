from functools import wraps
from bottle import request, redirect
from services.user_service import UserService   # buscar o objeto User

_user_service = UserService()

def login_required(func):

    # decorador: só deixa entrar se existir 'user' salvo na sessão Beaker e se não houver, redireciona para /login.

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        session = request.environ.get('beaker.session')
        if not session or 'user' not in session:
            return redirect('/login')
        return func(self, *args, **kwargs)
    return wrapper

def admin_required(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        session = request.environ.get('beaker.session')
        user = session.get('user') if session else None
        if not user:
            return redirect('/login?error= O usuário precisa estar logado')

        admin = user.get('adm')
        if not admin:
            return redirect('/login?error=Apenas admins podem criar eventos')   # TEM QUE COLOCAR O ERRO DE "SÓ ADMINS PODEM CRIAR EVENTOS"
        
        return func(self, *args, **kwargs)
    return wrapper

