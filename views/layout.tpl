<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!--acima foi definido o zoom, tamaho do site e charset-->
    <title>Tá marcado - {{title or 'Sistema'}}</title>
    <!--garante que sempre exista um titulo-->
    <link rel="stylesheet" href="/static/css/style.css" />
    <!--CSS no head-->
</head>
<body>
<nav class="navbar">
        <div class="container">
            <a class="navbar-brand" href="/">Tá Marcado</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav me-auto">
                    <li class="nav-item"> <a class="nav-link" href="/events">Eventos</a></li>
                    % if session and session.get('user'):
                        <!--quando tá logado-->
                        <li class="nav-item"><span class="nav-link">
                            % if session['user'].get('adm'):
                                <!--se for admin aparece uma estrelinha dourada-->
                                <span title="Admin" style="color: gold; margin-right: 5px;">&#11088;</span>
                            % end
                                Olá, <strong>{{session['user']['name']}}</strong> ({{session['user']['email']}}) </span></li>
                        <li class="nav-item"><a class="nav-link" href="/user">Perfil</a></li>
                        <li class="nav-item"><a class="nav-link" href="/logout">Logout</a> </li>
                        <!--falta fazer o /user com as coisas do user(poder ver eventos e sair)-->
                    % else:
                        <li class="nav-item">  <a class="nav-link" href="/login">Login</a> </li>
                        <li class="nav-item"> <a class="nav-link" href="/users/add">Cadastrar</a> </li>
                    % end
                </ul>
            </div>
        </div>

        
    </nav>
    <div class="container">
        {{!base}}  
        <!-- O conteúdo das páginas filhas virá aqui -->
        <!-- usar %rebase('layout.tpl', title='titulo-desejado') no arquivo que vai entrar aqui-->
        <!--apos isso, basta escrever o site, olhar users.tpl para ver exemplo-->
    </div>

    <footer> <!--aparece em toda pagina-->
        <p>&copy; 2025, Tá marcado. Todos os direitos reservados.</p>
    </footer>

    <!-- Scripts JS no final do body -->
    <script src="/static/js/main.js"></script>
</body>
</html>
