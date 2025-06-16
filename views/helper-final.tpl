<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Guia: Criar Nova Model - Activity</title>
    <!-- CSS para o tema -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github-dark.min.css">

    <!-- JS da biblioteca -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>

    <!-- Suporte a linguagens específicas (Python e HTML) -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/python.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/xml.min.js"></script>

    <!-- Ativa o realce automaticamente -->
    <script>hljs.highlightAll();</script>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            background: #f9f9f9;
            color: #333;
        }
        h1, h2 {
            color: #004d80;
        }
        pre {
            background: #f0f0f0;
            border-left: 4px solid #007acc;
            padding: 10px;
            overflow-x: auto;
        }
        code {
            font-family: Consolas, monospace;
        }
        section {
            margin-bottom: 40px;
        }
        .comment {
            background-color: #f8f8f8;
            padding: 15px;
            border-left: 4px solid #4CAF50;
            margin: 10px 0;
            font-style: italic;
        }
    </style>
</head>
<body>

<h1>Guia: Como Criar uma Nova Model no Projeto (Exemplo: Activity)</h1>

<div class="comment">
    <strong>Sobre este guia:</strong> Este documento explica como implementar uma nova entidade (Activity) seguindo o padrão MVC (Model-View-Controller) com separação em camadas (Model, Service, Controller e View). Cada seção contém o código necessário e explicações sobre seu funcionamento.
</div>

<section>
    <h2>1. Criar o Model</h2>
    
    <div class="comment">
        <strong>Função do Model:</strong> O model é responsável pela representação dos dados e persistência. Contém duas classes principais:<br>
        1. <strong>Activity</strong>: Representa a entidade com seus atributos e métodos de conversão<br>
        2. <strong>ActivityModel</strong>: Gerencia a persistência em arquivo JSON com operações CRUD completas
    </div>
    
    <pre><code class="language-python">class Activity:
    def __init__(self, id, name, description, done):
        self.id = id
        self.name = name
        self.description = description
        self.done = done

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'done': self.done
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)


class ActivityModel:
    FILE_PATH = 'data/activities.json'

    def __init__(self):
        self.activities = self._load()

    def _load(self):
        import json, os
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            return [Activity.from_dict(item) for item in json.load(f)]

    def _save(self):
        import json
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([a.to_dict() for a in self.activities], f, indent=4, ensure_ascii=False)

    def get_all(self):
        return self.activities

    def get_by_id(self, activity_id):
        return next((a for a in self.activities if a.id == activity_id), None)

    def add(self, activity):
        self.activities.append(activity)
        self._save()

    def update(self, updated_activity):
        for i, a in enumerate(self.activities):
            if a.id == updated_activity.id:
                self.activities[i] = updated_activity
                self._save()
                break

    def delete(self, activity_id):
        self.activities = [a for a in self.activities if a.id != activity_id]
        self._save()</code></pre>
</section>

<section>
    <h2>2. Criar o Service</h2>
    
    <div class="comment">
        <strong>Função do Service:</strong> Atua como intermediário entre controller e model, contendo:<br>
        - Lógica de negócio<br>
        - Conversão de tipos (ex: string para boolean)<br>
        - Validações básicas<br>
        - Gerenciamento de IDs sequenciais<br>
        Todas as operações delegam ao model a persistência real dos dados.
    </div>
    
    <pre><code class="language-python">from bottle import request
from models.activity import ActivityModel, Activity

class ActivityService:
    def __init__(self):
        self.activity_model = ActivityModel()

    def get_all(self):
        return self.activity_model.get_all()

    def save(self):
        last_id = max([a.id for a in self.activity_model.get_all()], default=0)
        new_id = last_id + 1
        name = request.forms.get('name')
        description = request.forms.get('description')
        done = request.forms.get('done') == 'on'
        activity = Activity(new_id, name, description, done)
        self.activity_model.add(activity)

    def get_by_id(self, activity_id):
        return self.activity_model.get_by_id(activity_id)

    def edit(self, activity):
        activity.name = request.forms.get('name')
        activity.description = request.forms.get('description')
        activity.done = request.forms.get('done') == 'on'
        self.activity_model.update(activity)

    def delete(self, activity_id):
        self.activity_model.delete(activity_id)
</code></pre>
</section>

<section>
    <h2>3. Criar o Controller</h2>
    
    <div class="comment">
        <strong>Função do Controller:</strong> Gerencia o fluxo da aplicação:<br>
        - Define rotas e mapeia para ações específicas<br>
        - Processa requisições HTTP (GET/POST)<br>
        - Coordena interação entre view e service<br>
        - Implementa redirecionamentos após ações<br>
        Herda de BaseController para funcionalidades comuns como renderização de templates.
    </div>
    
    <pre><code class="language-python">from bottle import Bottle, request
from .base_controller import BaseController
from services.activity_service import ActivityService

class ActivityController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.activity_service = ActivityService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/activities', method='GET', callback=self.list_activities)
        self.app.route('/activities/add', method=['GET', 'POST'], callback=self.add_activity)
        self.app.route('/activities/edit/&lt;activity_id:int&gt;', method=['GET', 'POST'], callback=self.edit_activity)
        self.app.route('/activities/delete/&lt;activity_id:int&gt;', method='POST', callback=self.delete_activity)

    def list_activities(self):
        activities = self.activity_service.get_all()
        return self.render('activities', activities=activities)

    def add_activity(self):
        if request.method == 'GET':
            return self.render('activity_form', activity=None, action='/activities/add')
        else:
            self.activity_service.save()
            self.redirect('/activities')

    def edit_activity(self, activity_id):
        activity = self.activity_service.get_by_id(activity_id)
        if request.method == 'GET':
            return self.render('activity_form', activity=activity, action=f'/activities/edit/{activity_id}')
        else:
            self.activity_service.edit(activity)
            self.redirect('/activities')

    def delete_activity(self, activity_id):
        self.activity_service.delete(activity_id)
        self.redirect('/activities')

activity_routes = Bottle()
activity_controller = ActivityController(activity_routes)</code></pre>
</section>

<section>
    <h2>4. Criar as Views</h2>
    
    <div class="comment">
        <strong>Sobre as Views:</strong> Templates que definem a interface do usuário:<br>
        - Utilizam sintaxe de template (Bottle SimpleTemplate)<br>
        - Separam lógica de apresentação<br>
        - São reutilizáveis (herdam de layout.tpl)<br>
        - Adaptam-se ao contexto (criação/edição)
    </div>

    <h3>4.1. <code>activities.tpl</code> — Listagem</h3>
    
    <div class="comment">
        <strong>Funcionalidades:</strong><br>
        - Lista todas atividades em tabela HTML<br>
        - Mostra status "Sim/Não" para tarefas concluídas<br>
        - Inclui links para edição e formulários de exclusão inline<br>
        - Botão para adicionar novas atividades
    </div>
    
    <pre><code class="language-html">{{'%'}} rebase('layout.tpl', title='Atividades')


&lt;h1&gt;Atividades&lt;/h1&gt;
&lt;a href=&quot;/activities/add&quot;&gt;Adicionar Atividade&lt;/a&gt;
&lt;table border=&quot;1&quot;&gt;
    &lt;tr&gt;
        &lt;th&gt;ID&lt;/th&gt;&lt;th&gt;Nome&lt;/th&gt;&lt;th&gt;Descrição&lt;/th&gt;&lt;th&gt;Feita?&lt;/th&gt;&lt;th&gt;Ações&lt;/th&gt;
    &lt;/tr&gt;
    {{'%'}} for a in activities:
    &lt;tr&gt;
        &lt;td&gt;{{'{{'}}a.id{{'}}'}}&lt;/td&gt;
        &lt;td&gt;{{'{{'}}a.name{{'}}'}}&lt;/td&gt;
        &lt;td&gt;{{'{{'}}a.description{{'}}'}}&lt;/td&gt;
        &lt;td&gt;{{'{{'}}'Sim' if a.done else 'Não'{{'}}'}}&lt;/td&gt;
        &lt;td&gt;
            &lt;a href=&quot;/activities/edit/{{'{{'}}a.id{{'}}'}}&quot;&gt;Editar&lt;/a&gt;
            &lt;form action=&quot;/activities/delete/{{'{{'}}a.id{{'}}'}}&quot; method=&quot;post&quot; style=&quot;display:inline;&quot;&gt;
                &lt;button type=&quot;submit&quot;&gt;Excluir&lt;/button&gt;
            &lt;/form&gt;
        &lt;/td&gt;
    &lt;/tr&gt;
    {{'%'}} end
&lt;/table&gt;
</code></pre>

    <h3>4.2. <code>activity_form.tpl</code> — Formulário</h3>
    
    <div class="comment">
        <strong>Funcionalidades:</strong><br>
        - Template único para criação e edição<br>
        - Detecta automaticamente o contexto (novo/edição)<br>
        - Preenche campos com valores existentes em modo edição<br>
        - Mantém ação (action) dinâmica para ambos os casos<br>
        - Inclui validação básica (campos required)<br>
        - Interface consistente com o layout base
    </div>
    
    <pre><code class="language-html">{{'%'}} rebase('layout.tpl', title='Nova Atividade' if not activity else 'Editar Atividade')


&lt;h1&gt;{{'{{'}}'Editar Atividade' if activity else 'Nova Atividade'{{'}}'}}&lt;/h1&gt;
&lt;form action=&quot;{{'{{'}}action{{'}}'}}&quot; method=&quot;post&quot;&gt;
    &lt;label&gt;Nome:&lt;br&gt;
        &lt;input type=&quot;text&quot; name=&quot;name&quot; value=&quot;{{'{{'}}activity.name if activity else ''{{'}}'}}&quot; required&gt;
    &lt;/label&gt;&lt;br&gt;&lt;br&gt;
    &lt;label&gt;Descrição:&lt;br&gt;
        &lt;textarea name=&quot;description&quot; required&gt;{{'{{'}}activity.description if activity else ''{{'}}'}}&lt;/textarea&gt;
    &lt;/label&gt;&lt;br&gt;&lt;br&gt;
    &lt;label&gt;
        &lt;input type=&quot;checkbox&quot; name=&quot;done&quot; {{'%'}} if activity and activity.done {{'%'}}checked{{'%'}} end&gt;
        Feita?
    &lt;/label&gt;&lt;br&gt;&lt;br&gt;
    &lt;button type=&quot;submit&quot;&gt;Salvar&lt;/button&gt;
&lt;/form&gt;
&lt;a href=&quot;/activities&quot;&gt;Voltar&lt;/a&gt;
</code></pre>
</section>

<div class="comment">
    <strong>Fluxo Completo do Sistema:</strong><br>
    1. <strong>Armazenamento</strong>: Dados persistidos em JSON pelo model<br>
    2. <strong>Operações</strong>: Service implementa lógica de negócio sobre o model<br>
    3. <strong>Rotas</strong>: Controller mapeia URLs para ações específicas<br>
    4. <strong>Interface</strong>: Views renderizam dados e capturam interações<br><br>
    <strong>Vantagens deste padrão:</strong><br>
    - Manutenção mais fácil<br>
    - Reuso de código<br>
    - Separação clara de responsabilidades<br>
    - Escalabilidade para novas funcionalidades
</div>

</body>
</html>