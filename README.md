#  Tá Marcado

 ![Logo Tá Marcado](/static/img/new_logo.png)

## ✅ Objetivo:
O projeto Tá Marcado é um sistema de gestão e compra de ingressos para eventos, que tem suporte a geração de QR Code como ingresso, login de usuários e painel administrativo e foi desenvolvido com Python (Bottle), HTML/CSS e persistência em JSON. 

Esse projeto tem como objetivo aplicar os conceitos de Programação Orientada a Objetos na construção de uma aplicação web realista e funcional utilizando Python com o microframework Bottle. A proposta é desenvolver um sistema completo de gerenciamento de eventos e vendas de ingressos, com funcionalidades como:

    Criação e administração de eventos;

    Cadastro e login de usuários com controle de permissões (cliente e administrador);

    Compra de ingressos com geração de QR Code;

    Interface com templates e persistência de dados em arquivos JSON.

A aplicação serve como base didática e extensível para estudos práticos de organização em camadas (MVC), uso de sessões, tratamento de exceções, manipulação de arquivos e interação com usuários por meio de uma interface web.



![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)

---

## 🚀 Funcionalidades

- ✅ Cadastro e login de usuários (clientes e administradores)
- 🔍 Busca de eventos por nome ou local (`/events/search?q=`)
- 🎫 Compra de ingressos com QR Code gerado automaticamente
- 📍 Detalhes completos do evento e endereço
- 🧾 Detalhamento do pagamento e download do ingresso
- 🔐 Proteção de rotas por tipo de usuário
- 🖼️ Upload de imagem de capa para os eventos
- 📑 Visualização do perfil com histórico de eventos
- 📈 Painel do administrador para criação de eventos
- ❤️ Curtidas nos eventos

---

## 🧠 Tecnologias Utilizadas

- **Backend:** Python + Bottle
- **Templates:** Bottle `template()` com extensão .tpl
- **Banco de Dados:** Simulação com arquivos `.json`
- **Frontend:** HTML, CSS, Bootstrap e Javascript
- **Outros:** Beaker Session, QRCode, Pylint, Pillow, os e Qrcode

---

## 📂 Estrutura de Pastas

```

epf-ta-marcado/
│
├── app.py # Inicialização da aplicação
├── controllers/ # Controladores de rotas
│ ├── auth_controller.py
│ ├── base_controller.py
│ ├── event_controller.py
│ ├── payment_controller.py
│ └── user_controller.py
│
├── models/ # Classes de domínio
│ ├── event.py
│ ├── payment.py
│ └── user.py
│
├── services/ # Lógica de negócio
│ ├── auth_service.py
│ ├── event_service.py
│ ├── payment_service.py
│ └── user_service.py
│
├── views/ # Páginas .tpl (templates Bottle)
│ ├── layout.tpl
│ ├── event_detail.tpl
│ ├── event_search.tpl
│ ├── events.tpl
│ ├── helper-final.tpl
│ ├── layout.tpl
│ ├── payment_detail.tpl
│ ├── payment_form.tpl
│ ├── payment_succes.tpl
│ ├── payments.tpl
│ ├── tickets.tpl
│ ├── user_form.tpl
│ ├── user.tpl
│ └── users.tpl
│
├── static/ # CSS, imagens e assets
│ ├── css/
│ ├── img/
│ └── uploads/
│
├── utils/ # Funções utilitárias
│ ├── decorators.py
│ ├── id_tracker.py
│ └── qr_code.py
│
└── data/ # Arquivos JSON com dados persistentes
├── users.json
├── events.json
├── last_ids.json
└── payments.json 

```


---

## Exemplo de Ingresso com QR Code

Ao confirmar o pagamento, o usuário recebe um QR Code com os dados do ingresso:

🎭 Musical Broadway: O Fantasma da Ópera
📅 Data: 19/02/2024 às 20:00
📍 Local: Teatro Municipal

💰 Total: R$ 300.00


---

# 📦 Como executar:

1. **Clone o repositório:**

```bash
git clone https://github.com/gus-ant/epf-ta-marcado.git
cd epf-ta-marcado
```

### Crie e ative o ambiente virtual:

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### Instale as dependências:

```bash
pip install -r requirements.txt
```

### Execute a aplicação:

```bash
python app.py
```

Abra no navegador: http://localhost:8080

# 📜 Requisitos

Estão no arquivo requirements.txt com:

    bottle
    beaker
    qrcode
    pillow
    pylint

### 🧪 Testes manuais

    Acesse como visitante, cliente e administrador

    Crie eventos e tente realizar compras

    Veja o funcionamento do QR Code e login

    Busque por eventos em /events/search?q=

### 🛠️ Possíveis melhorias futuras

    Integração com banco de dados real (SQLite, PostgreSQL)

    Upload de PDF dos ingressos

    Responsividade para mobile

    Sistema de cupons de desconto

    Filtros avançados na busca


### 🙋‍♂️ Autores

Feito com dedicação por Gabriel Velho e Gustavo Antonio

📚 Engenharia - FCTE/UnB
