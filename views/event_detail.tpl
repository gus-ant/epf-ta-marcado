%rebase('layout', title=event.name)


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
        
        % from datetime import datetime, timedelta
        % event_date = datetime.strptime(event.date, '%Y-%m-%d').date()
        % today = datetime.today().date()
        % if event_date < today:
            % label = '<span style="color: red; font-weight: bold;">(EXPIRADO)</span>'
        % elif event_date == today:
            % label = '<span style="color: green; font-weight: bold;">(HOJE)</span>'
        % elif event_date == today + timedelta(days=1):
            % label = '<span style="color: orange; font-weight: bold;">(AMANHÃ)</span>'
        % else:
            % label = ''
        % end
        <p>
          📅 {{event.date}} às {{event.time}} {{!label}} <br>
          📍 {{event.local}}
        </p>

        <div class="event-description">
          <h3>Sobre o Evento</h3>
          <p>{{event.description}}</p>
        </div>

        <div class="event-info-box">
          <h3>Informações do Evento</h3>
          <ul>
            % if event.price == 0 or event.price == None:
              <li><strong>Entrada:</strong> Grátis</li>
            % else:
              <li><strong>Valor:</strong> R$ {{'%.2f' % event.price}}</li>
            % end
            <li>
              <strong>Capacidade:</strong> {{event.current_capacity}} / {{event.max_capacity}}
              % if event.current_capacity <= 0:
                <span style="color: red; font-weight: bold; margin-left: 10px;">(Ingressos Esgotados)</span>
              % end
            </li>
            <li><strong>Id do organizador:</strong> {{event.owner_id}}</li>
          </ul>
        </div>

        <!-- Botões de interação -->
        % expired = event_date < today
        % sold_out = event.current_capacity <= 0

        <div class="event-actions">
          % if expired:
            <p class="alert alert-danger">⚠️ Evento Expirado. Inscrições encerradas.</p>
          % elif sold_out:
            <p class="alert alert-danger">⚠️ Acabaram os ingressos!</p>
          % else:
            % if user and not user.adm and user.id in event.participants_ids:
              <p class="alert alert-success">✅ Você já participa do evento, Tá Marcado!</p>
              <form action="/events/{{event.id}}/leave" method="post">
                <button type="submit" class="btn btn-danger">🚪 Sair do evento</button>
              </form>
            % elif user and not user.adm:
              <form action="/events/{{event.id}}/join" method="post">
                <button type="submit" class="btn btn-primary">❤️ Quero ir</button>
              </form>
            % elif user and user.adm:
              <p class="alert alert-warning">⚠️ Para se inscrever, use uma conta de usuario</p>
            % else:
              <form action="/events/{{event.id}}/join" method="post">
                <button type="submit" class="btn">🔐 Faça login para garantir seu ingresso</button>
              </form>
            % end
          % end
        </div>

        <!-- Participantes (somente admin) -->
        % if user and user.adm and user.id == event.owner_id:
          <div class="event-participants">
            <h3>id dos Participantes:</h3>

              <ul>
              % if len(event.participants_ids)>1:
                % for id in event.participants_ids:
                  <li> {{ id }}</li>
                % end
              % else:
                <p class="alert alert-warning"> Esse evento ainda não tem inscritos</p>

              </ul>
              
          </div>
        % end
      </div>
    </div>
  </div>
  