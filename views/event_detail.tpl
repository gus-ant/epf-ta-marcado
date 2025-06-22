%rebase('layout', title='Eventos') 

<h1>Evento: {{evento.name}}</h1>

<p><strong>Local:</strong> {{evento.local}}</p>
                <p><strong>Data:</strong> {{evento.date}} às {{evento.time}}</p>
                <p><strong>Preço:</strong> R$ {{evento.price}}</p>
                <p><strong>Capacidade:</strong> {{evento.current_capacity}} / {{evento.max_capacity}}</p>
                <form action="/events/{{evento.id}}/join" method="post" style="display:inline;">
                    <button type="submit">❤️ Quero ir</button>
                </form>
