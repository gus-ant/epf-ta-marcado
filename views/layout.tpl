<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!--acima foi definido o zoom, tamaho do site e charset-->
    <title>Sistema Bottle - {{title or 'Sistema'}}</title>
    <!--garante que sempre exista um titulo-->
    <link rel="stylesheet" href="/static/css/style.css" />
    <!--CSS no head-->
</head>
<body>
    <div class="container">
        {{!base}}  
        <!-- O conteúdo das páginas filhas virá aqui -->
        <!-- usar %rebase('layout.tpl', title='titulo-desejado') no arquivo que vai entrar aqui-->
        <!--apos isso, basta escrever o site, olhar users.tpl para ver exemplo-->
    </div>

    <footer> <!--aparece em toda pagina-->
        <p>&copy; 2025, Meu Projeto. Todos os direitos reservados.</p>
    </footer>

    <!-- Scripts JS no final do body -->
    <script src="/static/js/main.js"></script>
</body>
</html>
