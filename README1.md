#  Tá Marcado

Sistema de gestão e compra de ingressos para eventos, com suporte a geração de QR Code como ingresso, login de usuários e painel administrativo. Desenvolvido com Python (Bottle), HTML/CSS e persistência em JSON.

![Python](https://img.shields.io/badge/python-3.12-blue)
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
- **Templates:** Bottle `template()` com estilo Jinja2
- **Banco de Dados:** Simulação com arquivos `.json`
- **Frontend:** HTML5, CSS3, Bootstrap
- **Outros:** Beaker Session, QRCode e Pillow

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
│ ├── payment_detail.tpl
│ ├── user.tpl
│ └── ...
│
├── static/ # CSS, imagens e assets
│ ├── css/
│ ├── img/
│ └── uploads/
│
├── utils/ # Funções utilitárias
│ ├── decorators.py
│ └── qr_code.py
│
└── data/ # Arquivos JSON com dados persistentes
├── users.json
├── events.json
└── payments.json 
```


---

## Exemplo de Ingresso com QR Code

Ao confirmar o pagamento, o usuário recebe um QR Code com os dados do ingresso:

🎭 Musical Broadway: O Fantasma da Ópera
📅 Data: 19/02/2024 às 20:00
📍 Local: Teatro Municipal
🎟️ Ingresso: student /// Sugestão

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
    Pillow

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

### 📄 Licença

Este projeto está licenciado sob a licença MIT.

### 🙋‍♂️ Autor

Feito com dedicação por Gustavo Rodrigues

📚 Engenharia - FGA/UnB
🔗 GitHub | LinkedIn