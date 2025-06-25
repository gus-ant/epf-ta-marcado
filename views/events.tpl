
%rebase('layout', title='Eventos') 

<body>

<!-- Esse template mostra os eventos disponíveis, podendo ser no futuro a página inicial com a navbar para acessar o login/ cadastro-->

<!-- Tambem Já coloquei o coração para "curtir"evento como uma prévia-->

    <h1>Eventos Disponíveis</h1>

    % if eventos:
        <ul>
        % for evento in eventos:
            <li>
            <h2>
                <a href="/events/{{evento.id}}">{{evento.name}}</a>
            </h2>
                <p><strong>Local:</strong> {{evento.local}}</p>
                
                % if evento.price == 0:
                    <p><strong>Entrada grátis</strong></p>
                % else:
                    <p><strong>Preço:</strong> R$ {{evento.price}}</p>
                %end
                       
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
