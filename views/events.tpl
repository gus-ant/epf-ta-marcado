
%rebase('layout', title='Eventos') 

<body>

<!-- Esse template mostra os eventos disponíveis, podendo ser no futuro a página inicial com a navbar para acessar o login/ cadastro-->

<!-- Tambem Já coloquei o coração para "curtir"evento como uma prévia-->

    <h1>Eventos Disponíveis</h1>

    % if eventos:
        <ul>
        % for evento in eventos:
            <li>
                <h3>{{evento.name}}</h3>
                <p><strong>Local:</strong> {{evento.local}}</p>
                <p><strong>Data:</strong> {{evento.date}} às {{evento.time}}</p>
                <p><strong>Preço:</strong> R$ {{evento.price}}</p>
                <p><strong>Capacidade:</strong> {{evento.current_capacity}} / {{evento.max_capacity}}</p>
                <form action="/events/{{evento.id}}/join" method="post" style="display:inline;">
                    <button type="submit">❤️ Quero ir</button>
                </form>
            </li>
            <hr>
        % end
        </ul>
    % else:
        <p>Nenhum evento disponível no momento.</p>
    % end

    <a href="/events/create">+ Criar novo evento</a>
</body>
</html>
