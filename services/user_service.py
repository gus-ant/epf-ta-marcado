from bottle import request #usado pra acessar dados de formularios HTTP
from models.user import UserModel, User
from exceptions import EmailAlreadyUsedException

class UserService:
    # Esta classe atua como uma camada intermediária entre o controlador (rotas)
    #e o modelo de dados, implementando a lógica de negócio.: 

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
        
        if not password: #verifica se não foi colocada uma senha 
            raise ValueError("É obrigatorio ter uma senha")
        
        if self.user_model.get_by_email(email): #verifica se o email ja existe
            raise EmailAlreadyUsedException(email)

        user = User(id=new_id, name=name, email=email, birthdate=birthdate, password=password, adm=adm) #cria o objeto de user
        self.user_model.add_user(user) #adiciona na memoria



    def get_by_id(self, user_id):
        return self.user_model.get_by_id(user_id) #usa o metodo de user.py
    
    def get_by_email(self, email):
        return self.user_model.get_by_email(email) #usa o metodo de user.py


    def edit_user(self, user): #usa um objeto user
        name = request.forms.get('name') #puxa os dados do formulario http
        email = request.forms.get('email')
        birthdate = request.forms.get('birthdate')
        password = request.forms.get('password')
        adm = request.forms.get('adm')== 'on'

        existing_user = self.user_model.get_by_email(email) #verifica um user que já tem o mesmo email
        if existing_user and existing_user.id != user.id: #caso o email seja usado por outro user, raiser error
            raise EmailAlreadyUsedException(email)

        user.name = name #sobrescreve os dados
        user.email = email
        user.birthdate = birthdate
        user.adm = adm

        if password and password.strip(): #só troca de senha caso uma nova for fornecida
            user.set_password(password)

        self.user_model.update_user(user) #usa o metodo do user.py


    def delete_user(self, user_id):
        self.user_model.delete_user(user_id) #usa o metodo do user.py

    def authenticate(self, email, password):
        #autentica um usuario usando email e senha
        user = self.user_model.get_by_email(email)
        if user and user.check_password(password): #caso a senha for correta
            return user
        return None #caso for incorreta
    
    def get_admins(self): #retorna apenas os admins
        return self.user_model.get_admins()
    
    def get_regular_users(self): #retorna apenas usuarios comuns
        return self.user_model.get_regular_users()
    
    def can_create_events(self, user): #verifica se o usuario pode criar eventos
        return user and user.adm
    
    def promote_to_adm(self, user_id): #promove um user a adm, usando seu id
        user = self.get_by_id(user_id)
        if user:
            user.adm = True
            self.user_model.update_user(user)
            return True
        return False #caso não exista esse user
    
    def demove_from_adm(self, user_id): #remove adm de um user, usando seu id
        user = self.get_by_id(user_id)
        if user:
            user.adm = True
            self.user_model.update_user(user)
            return True
        return False #caso não exista esse user
    
