import json
import os
from dataclasses import dataclass, asdict
from typing import List

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
# Define o diretório onde os arquivos de dados serão armazenados
# __file__ é o caminho do arquivo atual, os.path.dirname pega o diretório pai
# '..' navega um nível acima na estrutura de pastas, 'data' é a pasta de destino
# Exemplo: se o arquivo atual está em '/projeto/models/user.py', DATA_DIR será '/projeto/data'

class User: #representa um usuario do sistema
    def __init__(self, id, name, email, birthdate):
        self.id = id #identificador unico
        self.name = name #nome completo
        self.email = email #endereçp de email
        self.birthdate = birthdate #data de nascimento em string 
        #depois adicionar senha e se é adm ou não


    def __repr__(self): #representação em string, serve pra debbuging
        return (f"User(id={self.id}, name='{self.name}', email='{self.email}', "
                f"birthdate='{self.birthdate}'")


    def to_dict(self): #pega o objeto e transforma em um dicionario, serve pro JSON
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'birthdate': self.birthdate
        }
    """Exemplo:
            user = User(1, 'João', 'joao@email.com', '1990-01-15')
            user.to_dict() retorna:
            {'id': 1, 'name': 'João', 'email': 'joao@email.com', 'birthdate': '1990-01-15'}"""


    @classmethod #metodo de classe
    def from_dict(cls, data): #pega um dicionario e usando o nome das chaves, puxa os valores
        return cls( #cls é a classe User, escrito de forma generica para seguir boas praticas (cls é uma variavel que sempre aponta para a classe atual)
            id=data['id'], #aqui, id recebe o valor da chave de nome 'id' no dicionario data
            name=data['name'],
            email=data['email'],
            birthdate=data['birthdate']
        )#retorna um objeto usando os valores do dicionario


class UserModel:
    # Define o caminho do arquivo JSON onde os dados dos usuários são persistidos
    # Utiliza os.path.join para garantir compatibilidade entre diferentes sistemas operacionais
    FILE_PATH = os.path.join(DATA_DIR, 'users.json')

    def __init__(self):
        self.users = self._load() #inicia a lista e armazena na memoria 


    def _load(self):
        if not os.path.exists(self.FILE_PATH): #verifica se existe no sistema
            return [] #caso não tenha, retorna uma lista vazia
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f: #abre o filepath no modo read e chama isso de f
            data = json.load(f) #data é json.load(f), f é a parte acima (carrega o conteudo JSON para uma lista de dicionarios)
            return [User(**item) for item in data] #os dicionarios são desempacotados em objetos User
        # Exemplo: {'id': 1, 'name': 'João'} vira User(id=1, name='João')


    def _save(self): #abre o filepath, no modo write (sobrescreve o conteudo anterior), com utf 8 e chama isso de f 
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([u.to_dict() for u in self.users], f, indent=4, ensure_ascii=False) #o dump salva as coisas em f (arquivo de destino)
            #tudo é salvo como dict (objeto User vira dict), indent=4 facilita a leitura, o ensure permite caracteres unicode


    def get_all(self):
        return self.users #retorna todos os users carregados na memoria


    def get_by_id(self, user_id: int): 
        return next((u for u in self.users if u.id == user_id), None) #busca pelo id, caso não encontre, retorna None
        #o next é otimizado, pois para assim que acha


    def add_user(self, user: User):
        self.users.append(user) #adiciona na lista
        self._save()


    def update_user(self, updated_user: User):
        for i, user in enumerate(self.users): #retorna o user(objeto) e o indice de cada user
            if user.id == updated_user.id: #caso os ids sejam iguais
                self.users[i] = updated_user #troca o antigo pelo novo usando o indice
                self._save() #salva
                break #fecha o loop


    def delete_user(self, user_id: int): #salva uma nova lista sem o id antigo
        self.users = [u for u in self.users if u.id != user_id] #cria uma lista excluindo o antigo
        self._save() #salva
