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
            
          📢 Eventos que você criou:
        % else:
           Eventos que você participa:
        % end
      </h2>

      % if not user.adm:
      <div style="margin-bottom: 20px;">
        <a href="/user/payments" class="btn" style="background-color: #f39c12; color: white">
          💳 Ver meus pagamentos
        </a>
    </div>
      % end

      % if events:
      <div style="overflow-x: auto; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); margin-top: 20px;">
        <table class="styled-table">
  <thead>
    <tr >
      <th style="padding: 10px; border: 1px solid #ccc;">Imagem</th>
      <th style="padding: 10px; border: 1px solid #ccc;">Nome</th>
      <th style="padding: 10px; border: 1px solid #ccc;">Data / Hora / Local</th>
      % if not user.adm:
        <th style="padding: 10px; border: 1px solid #ccc;">Ação</th>
      % end
    </tr>
  </thead>
  <tbody>
    % for event in events:
    <tr >
      <td >
        % if event.cover:
          <img src="/static/uploads/event_covers/{{event.cover}}" alt="cover" style="width: 100px; height: 50px; object-fit: cover; border-radius: 4px;">
        % else:
          <img src="/static/img/BottleLogo.png" alt="cover" style="width: 100px; height: 50px; object-fit: cover; border-radius: 4px;">
        % end
      </td>
      <td style="padding: 10px; border: 1px solid #ccc;">
        <a href="/events/{{event.id}}">{{event.name}}</a>
      </td>
      <td style="padding: 10px; border: 1px solid #ccc;">
        {{event.date}} às {{event.time}} ({{event.local}})
      </td>
      % if not user.adm:
      <td style="padding: 10px; border: 1px solid #ccc;">
        <a href="/payments/{{event.payment_id}}" class="btn" style="background-color: #4caf50; color: white; padding: 8px 12px; border-radius: 6px; text-decoration: none;">
          Ver QR Code
        </a>
      </td>
      % end
    </tr>
    % end
  </tbody>
</table>
</div>
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
  %if user.adm:
    <div style="margin-top: 40px; text-align: left;">
              <a href="/events/create" class="btn" style="background-color: #6c5ce7; color: white;">+ Criar novo evento</a>
    </div>
  % end
    <div class="profile-actions">
      <a class="btn btn-edit" href="/users/edit/{{user.id}}">✏️ Editar Perfil</a>
      <a class="btn btn-secondary" href="/events"> Voltar</a>

    </div>
  </div>
</section>
