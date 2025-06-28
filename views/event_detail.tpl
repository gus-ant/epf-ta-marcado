%rebase('layout', title='Eventos') 

<h1>Evento: {{event.name}}</h1>

% if event.cover:
    <img src="/static/uploads/event_covers/{{event.cover}}" style="max-width: 300px;">
% end

<p><strong>Local:</strong> {{event.local}}</p>
                <p><strong>Data:</strong> {{event.date}} às {{event.time}}</p>
                % if event.price == 0:
                    <p><strong>Entrada grátis</strong></p>
                % else:
                    <p><strong>Preço:</strong> R$ {{event.price}}</p>
                % end
                <p><strong>Capacidade:</strong> {{event.current_capacity}} / {{event.max_capacity}}</p>
                <p><strong>Descrição:</strong> {{event.description}}</p>
                <p><strong>Email do criador do evento:</strong> {{event.owner_email}}</p>
                % if not user.adm:
                    <form action="/events/{{event.id}}/join" method="post" style="display:inline;">
                        <button type="submit">❤️ Quero ir</button>
                    </form>

