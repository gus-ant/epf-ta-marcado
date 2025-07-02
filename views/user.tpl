%rebase('layout', title='Perfil')



<section class="profile">
  <div class="container">
    <h1 class="section-title">👤 Perfil de {{ user.name }}</h1>

    <div class="profile-info card">
      <p><strong>Nome:</strong> {{ user.name }}</p>
      <p><strong>Email:</strong> {{ user.email }}</p>
      <p><strong>Data de nascimento:</strong> {{ user.birthdate }}</p>
      <p><strong>Senha:</strong> ********</p>
      <p>
        <strong>Tipo de conta:</strong> {{ 'Adm' if user.adm else 'Comum' }}
        % if user.adm:
          <span title="Admin" style="color: gold;">&#11088;</span>
        % end
      </p>
    </div>

    <div class="profile-events">
      <h2 class="section-title">
        % if user.adm:
          <div class="container">
            <div style="margin-top: 40px; text-align: left;">
              <a href="/events/create" class="btn" style="background-color: #3498db; color: white;">+ Criar novo evento</a>
            </div>
          📢 Eventos que você criou:
        % else:
           Eventos que você participa:
        % end
      </h2>

      % if not user.adm:
      <div style="margin-bottom: 20px;">
        <a href="/user/payments" class="btn" style="background-color: #f39c12; color: white">
          💳🧾 Ver meus pagamentos
        </a>
      </div>
      % end

      % if events:
        <ul class="event-list">
          % for event in events:
            <li style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
              % if event.cover:
                <img src="/static/uploads/event_covers/{{event.cover}}" alt="cover" style="width: 50px; height: 50px; object-fit: cover; border-radius: 4px;">
              % else:
                <div style="width: 50px; height: 50px; background: #ccc; border-radius: 4px;"></div>
              % end
              <a href="/events/{{event.id}}">{{event.name}}</a>
              <span class="muted">— {{event.date}} às {{event.time}} ({{event.local}})</span>
              % if not user.adm:
              <a href="/payments/{{event.payment_id}}" class="btn" style="background-color: #4caf50; color: white; padding: 8px 12px; border-radius: 6px; text-decoration: none;">
                Ver QR Code
              </a>
              % end
              
            </li>
          % end
        </ul>
      % else:
        <p class="muted">
          % if user.adm:
            Você ainda não criou nenhum evento.
          % else:
            Você ainda não participa de nenhum evento.
          % end
        </p>
      % end
    </div>

    <div class="profile-actions">
      <a class="btn btn-edit" href="/users/edit/{{user.id}}">✏️ Editar Perfil</a>
      <a class="btn btn-secondary" href="/events"> Voltar</a>
    </div>
  </div>
</section>
