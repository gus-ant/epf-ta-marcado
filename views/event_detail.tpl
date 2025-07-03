%rebase('layout', title=event.name)

<section class="section">
  <div class="container">

    <div class="event-detail-card">
      % if event.cover:
        <img src="/static/uploads/event_covers/{{event.cover}}" style="max-width: 400px; max-height: 300px;" alt="Capa do evento {{event.name}}">
      % else:
        <img src="/static/img/default-event.jpg" alt="Evento sem imagem">
      % end

      <div class="event-info">
        <h2 class="section-title">{{event.name}}</h2>

        <p><strong>Local:</strong> {{event.local}}</p>
        <p><strong>Data:</strong> {{event.date}} às {{event.time}}</p>

        % if event.price == 0:
          <p><strong>Entrada grátis</strong></p>
        % else:
          <p><strong>Preço:</strong> R$ {{event.price}}</p>
        % end

        <p><strong>Capacidade:</strong> {{event.current_capacity}} / {{event.max_capacity}}</p>
        <p><strong>Descrição:</strong> {{event.description}}</p>
        <p style="font-size: 0.9rem; color: var(--muted-text-color);">
          <strong>Email do criador:</strong> {{event.owner_email}}
        </p>

        % if user and user.adm and user.email == event.owner_email:
          <div class ="event-participants">
            <h2 class="section-title">Email dos participantes do evento:</h2>
            % for email in event.participants_emails:
              <p class="text">{{ email }}</p>
          </div>
            % end
        % end

        <!-- Lógica para botão ou mensagem -->
        <div style="margin-top: 20px;">
          % if user and not user.adm and user.email in event.participants_emails:
            <p class="alert alert-warning"> ✅ Você já participa do evento </p>
            <form action="/events/{{event.id}}/leave" method="post">
              <button type="submit" class="btn btn-warning">🚪 Sair do evento</button>
            </form>
          % elif user and not user.adm:
            <form action="/events/{{event.id}}/join" method="post">
              <button type="submit" class="btn">❤️ Quero ir</button>
            </form>
          % elif user and user.adm:
            <p class="alert alert-warning">⚠️ Para se inscrever, use um conta de cliente.</p>
          % else:
            <form action="/events/{{event.id}}/join" method="post">
              <button type="submit" class="btn">Faça login para garantir seu ingresso</button>
            </form>
          % end
        </div>
      </div>
    </div>

  </div>
</section>
