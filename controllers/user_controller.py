from bottle import Bottle, request
from .base_controller import BaseController
from services.user_service import UserService

class UserController(BaseController): #herda de BaseController

    def __init__(self, app):
        super().__init__(app) #chama o construtor da classe pai

        self.setup_routes()
        self.user_service = UserService()


    
    def setup_routes(self): # Rotas User
        self.app.route('/users', method='GET', callback=self.list_users) #Registra rota GET /users que chama o método list_users para listar usuários
        self.app.route('/users/add', method=['GET', 'POST'], callback=self.add_user) #Registra rota /users/add que aceita GET (mostrar formulário) e POST (salvar usuário)
        self.app.route('/users/edit/<user_id:int>', method=['GET', 'POST'], callback=self.edit_user) #Registra rota /users/edit/<user_id> com parâmetro inteiro para editar usuário específico
        self.app.route('/users/delete/<user_id:int>', method='POST', callback=self.delete_user) #Registra rota POST /users/delete/<user_id> para deletar usuário específico

        #novas rotas para gerenciar privilegios
        self.app.route('/users/promote/<user_id:int>', method='POST', callback=self.promote_user) #Promove usuário a admin
        self.app.route('/users/demote/<user_id:int>', method='POST', callback=self.demote_user) #Remove privilégios de admin

    def list_users(self):
        users = self.user_service.get_all() #users é a lista de todos os users
        return self.render('users', users=users) #renderiza o template users passando a lista de usuarios


    def add_user(self):
        if request.method == 'GET':
            return self.render('user_form', user=None, action="/users/add") #faz o formulario vazio para o novo usuario
        else:
            # POST - salvar usuário
            try:
                self.user_service.save()
                self.redirect('/users') #apos salvar manda de volta pra users
            except ValueError as e:
                # para tratar os erros
                return self.render('user_form', user=None, action='/users/add', error=str(e))


    def edit_user(self, user_id): #serve pra editar um usuario existente, usa o id
        user = self.user_service.get_by_id(user_id) #busca pelo id
        if not user:
            return "Usuário não encontrado" #retorna isso caso não exista esse usuario

        if request.method == 'GET':
            return self.render('user_form', user=user, action=f"/users/edit/{user_id}")
        else:
            # POST - salvar edição
            try:
                self.user_service.edit_user(user)
                self.redirect('/users')
            except ValueError as e:
                return self.render('user_form', user=user, action=f"/users/edit/{user_id}")


    def delete_user(self, user_id):
        self.user_service.delete_user(user_id) #remove o user
        self.redirect('/users') #redireciona 

    def promote_user(self, user_id):
        if self.user_service.promote_to_adm(user_id):
            return self.redirect('/users')
        else:
            return "Erro ao promover usuario"
    
    def demote_user(self, user_id):
        if self.user_service.demove_from_adm(user_id):
            return self.redirect('/users')
        else:
            return "Erro ao promover usuario"

user_routes = Bottle()
user_controller = UserController(user_routes)
