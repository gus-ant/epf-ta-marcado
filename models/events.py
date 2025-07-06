import json
import os
from dataclasses import dataclass, asdict
from typing import List
from datetime import datetime

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
# Define o diretório onde os arquivos de dados serão armazenados
# __file__ é o caminho do arquivo atual, os.path.dirname pega o diretório pai
# '..' navega um nível acima na estrutura de pastas, 'data' é a pasta de destino
# Exemplo: se o arquivo atual está em '/projeto/models/events.py', DATA_DIR será '/projeto/data'

class Event:
    #falta adicionar uma lista com todas as pessoas participando 

    def __init__(self, id, name, local, date, price, max_capacity, time, owner_id, description, cover=None, participants_ids:List[int]=None):
        self.id = id #identificador unico 
        self.name = name #nome do evento
        self.local = local #local do evento
        self.date = date #data do evento
        self.price = price #preço do ingresso
        self.max_capacity = max_capacity #capacidade maxima
        self.time = time #horario do envento
        self.owner_id = owner_id #email de quem criou o evento
        self.description = description #descrição do evento
        self.cover = cover #capa do evento
        self.participants_ids = participants_ids if participants_ids else [] #todos os emails dos participantes do evento

    @property
    def current_capacity(self):
        return self.max_capacity - len([e for e in self.participants_ids if e is not None])
    
    def __repr__(self): #representação em string 
        return (f"Event(id={self.id}, name={self.name}, local={self.local},time={self.time} ,"
                f"date={self.date}, price={self.price}, max_capacity={self.max_capacity},"
                f"owner_id={self.owner_id}),"
                f"description={self.description}")

    def to_dict(self): #torna o objeto em um dicionario
        return {
            'id': self.id,
            'name': self.name,
            'local': self.local,
            'date': self.date,
            'price': self.price,
            'max_capacity': self.max_capacity,
            'time' : self.time,
            'owner_id': self.owner_id,
            'description': self.description,
            'cover': self.cover,
            'participants_ids': self.participants_ids
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
            owner_id = data['owner_id'],
            description = data['description'],
            cover = data['cover'],
            participants_ids = data.get('participants_ids', [])
        ) 

class EventModel:
    FILE_PATH = os.path.join(DATA_DIR, 'events.json')
    #Define o caminho do arquivo JSON onde os dados dos eventos são persistidos
    #os.path.join para garantir compatibilidade entre sistemas operacionais
    
    def __init__(self):
        self.events = self._load() #inicializa a lista e armazena na memoria

    def _load(self):
        if not os.path.exists(self.FILE_PATH): #caso não tenha
            return [] #lista vazia

        with open(self.FILE_PATH, 'r', encoding='utf-8') as f: #abre o arquivo em modo read e chama isso de f
            content = f.read().strip()
            if not content or content == "":  # EVITA erro com arquivo vazio
                return [] # isso faz retornar uma lista vazia se o Arquivo existir mas não tiver nada
            try:
                data = json.loads(content) #carrega o conteudo json do arquivo 'content'
                return [Event(**item) for item in data] #os dicionarios do arquivo são desempacotados em objetos Event
            except json.JSONDecodeError:
                print("Erro ao carregar JSON do arquivo de eventos. Verifique o conteúdo.")
                return []
        
    def _save(self):
        os.makedirs(os.path.dirname(self.FILE_PATH), exist_ok=True) #faz o diretorio caso ainda não exista

        with open(self.FILE_PATH, 'w', encoding='utf-8') as f: #abre o arquivo file_path no modo de write e chama isso de f
            json.dump([e.to_dict() for e in self.events], f, indent=4, ensure_ascii=False)
        #tudo é salvo como dict (objeto Event vira dict (posteriormente vai voltar a ser objeto))
        # f é o arquivo, indent é pra facilitar a leitura, ensure ascii false permite caracteres unicode

    def get_all(self): #retorna todos
        self.events = self._load()
        return self.events
    
    def get_by_id(self, event_id:int):
        self.events = self._load()
        return next((e for e in self.events if e.id == event_id), None)
    #retorna o evento com o mesmo id, caso não exista, None
    #next é otimizado, por parar quando acha

    def get_by_owner_id(self, event_owner_id:int):
        return [e for e in self.events if e.owner_id == event_owner_id]
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
        self.events = self._load()

    def update_event(self, updated_event: Event):
        for i, event in enumerate(self.events): #busca o evento e a ordem dele na lista
            if event.id == updated_event.id: #se os eventos tiverem o id igual
                self.events[i] = updated_event #troca o evento da lista pelo novo
                self._save() #salva
                print(f"[UPDATE] Evento salvo {updated_event.name}.")
                print(f"lista de emails: {updated_event.participants_ids}")
                self.events = self._load()
                break #fecha o loop
    
    def delete_event(self, event_id:int):
        self.events = [e for e in self.events if e.id !=event_id] #troca por uma nova lista sem o item com mesmo id
        self._save() #salva
        self.events = self._load()
    
    def get_participants(self, event_id:int):
        self.events = self._load()
        event = self.get_by_id(event_id)
        return event.participants_ids if event else []  
    
    def get_participants_number(self, event_id:int):
        self.events = self._load()
        event = self.get_by_id(event_id)
        if not event:
            return 0
        return len([e for e in event.participants_ids if e is not None]) #só pega ids nao vazios
    
    def get_15_next_events(self):
        self.events = self._load()
        hoje = datetime.today().date() #pega o dia atual
        eventos_futuros = [e for e in self.events if datetime.strptime(e.date, "%Y-%m-%d").date() >= hoje] #só eventos que ainda não ocorreram
        eventos_em_ordem = sorted(eventos_futuros, key=lambda e: datetime.strptime(e.date, "%Y-%m-%d").date()) #ordena por data
        return eventos_em_ordem[:15] #retorna os 15 mais novos 
    
    def get_future_events(self):
        hoje = datetime.today().date()
        return [e for e in self.events if datetime.strptime(e.date, "%Y-%m-%d").date() >= hoje]
    
    def get_past_events(self):
        hoje = datetime.today().date()
        return [e for e in self.events if datetime.strptime(e.date, "%Y-%m-%d").date() < hoje]
    
    def get_top_15_events(self):
        self.events = self._load()
        eventos = self.get_future_events() #só usa eventos que ainda n ocorreram

        eventos_ordem_participantes = sorted(
            eventos, #usa eventos
            key=lambda e: self.get_participants_number(e.id), #ordena por quantos participantes tem
            reverse=True #inverte, pra manter a ordem certa
        )

        return eventos_ordem_participantes[:15]