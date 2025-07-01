from bottle import static_file #usado pro CSS

class BaseController: #classe base para todos os controllers

    def __init__(self, app):
        self.app = app
        self._setup_base_routes()


    def _setup_base_routes(self): #configura rotas basicas, serão herdadas
        """Configura rotas básicas comuns a todos os controllers"""
        
        self.app.route('/', method='GET', callback=self.home_redirect) 
        # Registra a rota raiz '/' com método GET
        # Quando alguém acessar http://localhost:8080/, chama self.home_redirect
        
        self.app.route('/helper', method=['GET'], callback=self.helper)
        # Registra a rota '/helper' com método GET
        # method=['GET'] é uma lista, permitindo múltiplos métodos HTTP se necessário
        # Quando acessar /helper, chama self.helper

        
        self.app.route('/static/<filename:path>', callback=self.serve_static)
        # Rota para arquivos estáticos (CSS, JS, imagens)# <filename:path> captura qualquer caminho após /static/
        # Exemplo: /static/css/style.css → filename = 'css/style.css'
        # :path permite capturar caminhos com barras (subpastas)


    def home_redirect(self):
        """Redireciona a rota raiz para /users"""
        return self.redirect('/events') #em algum momento isso vai mudar para /home


    def helper(self): #pagina de ajuda/documentação
        return self.render('helper-final')
    # Chama o método render para processar o template 'helper-final'
    # Procura por arquivo helper-final.tpl na pasta de templates


    def serve_static(self, filename): #filename é o caminho do arquivo
        """Serve arquivos estáticos (CSS) da pasta static/"""
        return static_file(filename, root='./static')
        # static_file é uma função do Bottle que:
        # - Procura o arquivo 'filename' na pasta './static'
        # - Define o Content-Type correto automaticamente
        # - Retorna o conteúdo do arquivo ou erro 404
        # root='./static' define a pasta raiz dos arquivos estáticos


    def render(self, template, **context): #template é o nome, **context: Argumentos nomeados que serão passados para o template
        """Método auxiliar para renderizar templates HTML"""
        from bottle import template as render_template, request
        session = request.environ.get('beaker.session') #pega a sessao atual
        context['session'] = session #passa pro html
        # Importa a função template do Bottle (renomeada para render_template)
        # Importação local evita conflitos de nomes e melhora performance
        return render_template(template, **context)
        # Chama a função de template do Bottle
        # template: nome do arquivo .tpl
        # **context: desempacota argumentos nomeados para o template


    def redirect(self, path): #serve pra fazer os redirecionamentos
        """Método auxiliar para redirecionamento"""
        from bottle import redirect as bottle_redirect
        return bottle_redirect(path)
