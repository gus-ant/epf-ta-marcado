import os
import json

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data') #pasta
LAST_ID_FILE = os.path.join(DATA_DIR, 'last_ids.json') #arquivo

def ensure_last_id_file():
    if not os.path.exists(LAST_ID_FILE): #caso não tenha banco de dados
        os.makedirs(DATA_DIR, exist_ok=True) #cria o diretorio
        with open(LAST_ID_FILE, 'w') as f: #abre
            json.dump({"event_id":0, "user_id":0}, f) #salva os 2 como 0

def get_next_id(key:str):
    ensure_last_id_file()
    with open(LAST_ID_FILE, 'r') as f:
        data = json.load(f) #carrega as coisas do arquivo

    last_id = data.get(key, 0) +1 #last id é o id mais velho +1
    data[key] = last_id #troca o id velho

    with open(LAST_ID_FILE, 'w') as f:
        json.dump(data, f, indent=4) #salva o id novo mais alto

    return last_id #retorna o id mais novo