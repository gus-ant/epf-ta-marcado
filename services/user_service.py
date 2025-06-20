from bottle import request #usado pra acessar dados de formularios HTTP
from models.user import UserModel, User

class UserService:
    # Esta classe atua como uma camada intermediária entre o controlador (rotas)
    #e o modelo de dados, implementando a lógica de negócio.

    def __init__(self):
        self.user_model = UserModel() #acessa o usermodel de user.py


    def get_all(self):
        users = self.user_model.get_all() #usa o metodo de user.py
        return users


    def save(self):
        last_id = max([u.id for u in self.user_model.get_all()], default=0) #encontra o id mais alto do sistema
        new_id = last_id + 1 #soma 1 ao ultimo id gerado
        name = request.forms.get('name') #pega esse dado diretamente do formulario http
        email = request.forms.get('email')
        birthdate = request.forms.get('birthdate')
        password = request.forms.get('password') #puxa a senha do formulario
        adm = request.forms.get('adm') == 'on' #é um checkbox, on se marcado, none se não 

        user = User(id=new_id, name=name, email=email, birthdate=birthdate) #cria o objeto de user
        self.user_model.add_user(user) #adiciona na memoria


    def get_by_id(self, user_id):
        return self.user_model.get_by_id(user_id) #usa o metodo de user.py


    def edit_user(self, user): #usa um objeto user
        name = request.forms.get('name') #puxa os dados do formulario http
        email = request.forms.get('email')
        birthdate = request.forms.get('birthdate')

        user.name = name #sobrescreve os dados
        user.email = email
        user.birthdate = birthdate

        self.user_model.update_user(user) #usa o metodo do user.py


    def delete_user(self, user_id):
        self.user_model.delete_user(user_id) #usa o metodo do user.py
