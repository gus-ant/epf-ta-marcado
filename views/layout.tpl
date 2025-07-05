<!DOCTYPE html>
<html lang="pt-br">

<!--Coloquei o CSS no head do Layout.tpl pq não estava conseguindo modificar direto no arquivo style.css-->

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tá marcado - {{title or 'Sistema'}}</title>

  <link  href="/static/css/style.css" rel="stylesheet"/>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet" />

</head>

<body>
  <nav class="navbar">
      <a class="navbar-brand" href="/">
        <img src="/static/img/new_logo.png" alt="Tá Marcado Logo" style="height: 36px;" />
        Tá Marcado
      </a>

      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav me-auto">
          <li class="nav-item"><a class="nav-link" href="/events">Eventos</a></li>
          % if session and session.get('user'):
            <li class="nav-item"><span class="nav-link">
              % if session['user'].get('adm'):
                <span title="Admin" style="color: gold; margin-right: 5px;">&#11088;</span>
              % end
              Olá, <strong>{{session['user']['name']}}</strong> 
            </span></li>
            <li class="nav-item"><a class="nav-link" href="/user">Perfil</a></li>
            <li class="nav-item"><a class="nav-link" href="/logout">Logout</a></li>
          % else:
            <li class="nav-item"><a class="nav-link" href="/login">Login</a></li>
            <li class="nav-item"><a class="nav-link" href="/users/add">Cadastrar</a></li>
          % end
        </ul>
      </div>
    
  </nav>


    {{!base}}
    

  <footer>
    <p>&copy; 2025, Tá Marcado. Todos os direitos reservados.</p>
  </footer>

  <script src="/static/js/main.js"></script>
</body>
</html>
