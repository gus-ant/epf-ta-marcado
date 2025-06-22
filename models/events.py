import json
import os
from dataclasses import dataclass, asdict
from typing import List

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
# Define o diretório onde os arquivos de dados serão armazenados
# __file__ é o caminho do arquivo atual, os.path.dirname pega o diretório pai
# '..' navega um nível acima na estrutura de pastas, 'data' é a pasta de destino
# Exemplo: se o arquivo atual está em '/projeto/models/events.py', DATA_DIR será '/projeto/data'

class Event:
    #falta adicionar uma lista com todas as pessoas participando 

    def __init__(self, id, name, local, date, price, max_capacity, time, current_capacity, owner_email):
        self.id = id #identificador unico 
        self.name = name #nome do evento
        self.local = local #local do evento
        self.date = date #data do evento
        self.price = price #preço do ingresso
        self.max_capacity = max_capacity #capacidade maxima
        self.time = time #horario do envento
        self.owner_email = owner_email #email de quem criou o evento

        self.current_capacity = max_capacity #capacidade atual inicial
        if current_capacity != None: #caso seja passado valor
            self.current_capacity = current_capacity
        #(posteriormente calcular quando alguem entrar ou sair do evento)
    
    def __repr__(self): #representação em string 
        return (f"Event(id={self.id}, name={self.name}, local={self.local},time={self.time} ,"
                f"date={self.date}, price={self.price}, max_capacity={self.max_capacity},"
                 f"owner_email={self.owner_email}), current_capacity={self.current_capacity}")

    def to_dict(self): #torna o objeto em um dicionario
        return {
            'id': self.id,
            'name': self.name,
            'local': self.local,
            'date': self.date,
            'price': self.price,
            'max_capacity': self.max_capacity,
            'time' : self.time,
            'current_capacity': self.current_capacity,
            'owner_email': self.owner_email
        }

    @classmethod #metodo de classe
    def from_dict(cls, data):
        return cls(
            id = data['id'],
            name = data['name'],
            local = data['local'],
            date = data['date'],
            price = data['price'],
            max_capacity = data['max_capacity'],
            time = data['time'],
            current_capacity = data['current_capacity'],
            owner_email = data['owner_email']
        ) 

class EventModel:
    FILE_PATH = os.path.join(DATA_DIR, 'events.json')
    #Define o caminho do arquivo JSON onde os dados dos eventos são persistidos
    #os.path.join para garantir compatibilidade entre sistemas operacionais
    
    def __init__(self):
        self.events = self._load() #inicializa a lista e armazena na memoria

    def _load(self):
        if not os.path.exists(self.FILE_PATH): #caso não tenha
            return[] #lista vazia
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f: #abre o arquivo em modo read e chama isso de f
            data = json.load(f) #data é json.load(f) f é o arquivo
            return [Event(**item) for item in data] #os dicionarios do arquivo são desempacotados em objetos Event
        
    def _save(self):
        os.makedirs(os.path.dirname(self.FILE_PATH), exist_ok=True) #faz o diretorio caso ainda não exista

        with open(self.FILE_PATH, 'w', encoding='utf-8') as f: #abre o arquivo file_path no modo de write e chama isso de f
            json.dump([e.to_dict() for e in self.events], f, indent=4, ensure_ascii=False)
        #tudo é salvo como dict (objeto Event vira dict (posteriormente vai voltar a ser objeto))
        # f é o arquivo, indent é pra facilitar a leitura, ensure ascii false permite caracteres unicode

    def get_all(self): #retorna todos
        return self.events
    
    def get_by_id(self, event_id:int):
        return next((e for e in self.events if e.id == event_id), None)
    #retorna o evento com o mesmo id, caso não exista, None
    #next é otimizado, por parar quando acha

    def get_by_owner_email(self, event_owner_email:str):
        return [e for e in self.events if e.owner_email == event_owner_email]
    #retorna lista com eventos que tenham owner_email =

    def get_by_name(self, event_name:str): 
        return [e for e in self.events if e.name == event_name]
    #retorna lista com eventos que tenham name=

    def get_open_events(self):
        return [e for e in self.events if e.current_capacity != 0]
    #retorna lista com todos os eventos que ainda tenham vagas

    def get_closed_events(self):
        return [e for e in self.events if e.current_capacity == 0]
    #retorna lista com todos os eventos fechados

    def add_event(self, event:Event):
        self.events.append(event) #adiciona na lista
        self._save()

    def update_event(self, updated_event: Event):
        for i, event in enumerate(self.events): #busca o evento e a ordem dele na lista
            if event.id == updated_event.id: #se os eventos tiverem o id igual
                self.events[i] = updated_event #troca o evento da lista pelo novo
                self._save() #salva
                break #fecha o loop
    
    def delete_event(self, event_id:int):
        self.events = [e for e in self.events if e.id !=event_id] #troca por uma nova lista sem o item com mesmo id
        self._save() #salva

