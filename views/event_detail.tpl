%rebase('layout', title='Eventos') 

<h1>Evento: {{evento.name}}</h1>

% if evento.cover:
    <img src="/static/uploads/event_covers/{{evento.cover}}" style="max-width: 300px;">
% end

<p><strong>Local:</strong> {{evento.local}}</p>
                <p><strong>Data:</strong> {{evento.date}} às {{evento.time}}</p>
                % if evento.price == 0:
                    <p><strong>Entrada grátis</strong></p>
                % else:
                    <p><strong>Preço:</strong> R$ {{evento.price}}</p>
                % end
                <p><strong>Capacidade:</strong> {{evento.current_capacity}} / {{evento.max_capacity}}</p>
                <p><strong>Descrição:</strong> {{evento.description}}</p>
                <p><strong>Email criador do evento:</strong> {{evento.owner_email}}</p>
                <form action="/events/{{evento.id}}/join" method="post" style="display:inline;">
                    <button type="submit">❤️ Quero ir</button>
                </form>

