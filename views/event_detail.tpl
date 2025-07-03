%rebase('layout', title=event.name)

<section class="section">
  <div class="container">
    <div class="event-detail-grid">
      
      <!-- Imagem do evento -->
      <div class="event-cover-box">
        % if event.cover:
          <img src="/static/uploads/event_covers/{{event.cover}}" alt="Capa do evento {{event.name}}" class="event-cover-img">
        % else:
          <img src="/static/img/BottleLogo.png" alt="Evento sem imagem" class="event-cover-img">
        % end
      </div>

      <!-- Informações do evento -->
      <div class="event-content-box">
        <h1 class="event-title">{{event.name}}</h1>
        
        <p class="event-meta">
          📅 {{event.date}} às {{event.time}} <br>
          📍 {{event.local}}
        </p>

        <div class="event-description">
          <h3>Sobre o Evento</h3>
          <p>{{event.description}}</p>
        </div>

        <div class="event-info-box">
          <h3>Informações do Evento</h3>
          <ul>
            % if event.price == 0:
              <li><strong>Entrada:</strong> Grátis</li>
            % else:
              <li><strong>Valor:</strong> R$ {{event.price}}</li>
            % end
            <li><strong>Capacidade:</strong> {{event.current_capacity}} / {{event.max_capacity}}</li>
            <li><strong>Email do organizador:</strong> {{event.owner_email}}</li>
          </ul>
        </div>

        <!-- Botões de interação -->
        <div class="event-actions">
          % if user and not user.adm and user.email in event.participants_emails:
            <p class="alert alert-success">✅ Você já participa do evento.</p>
            <form action="/events/{{event.id}}/leave" method="post">
              <button type="submit" class="btn btn-danger">🚪 Sair do evento</button>
            </form>
          % elif user and not user.adm:
            <form action="/events/{{event.id}}/join" method="post">
              <button type="submit" class="btn btn-primary">❤️ Quero ir</button>
            </form>
          % elif user and user.adm:
            <p class="alert alert-warning">⚠️ Para se inscrever, use uma conta de cliente.</p>
          % else:
            <form action="/events/{{event.id}}/join" method="post">
              <button type="submit" class="btn btn-outline">🔐 Faça login para garantir seu ingresso</button>
            </form>
          % end
        </div>

        <!-- Participantes (somente admin) -->
        % if user and user.adm and user.email == event.owner_email:
          <div class="event-participants">
            <h3>Participantes</h3>
            <ul>
              % for email in event.participants_emails:
                <li>📧 {{ email }}</li>
              % end
            </ul>
          </div>
        % end
      </div>
    </div>
  </div>
</section>
