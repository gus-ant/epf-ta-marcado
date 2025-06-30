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
          📢 Eventos que você criou
        % else:
           Eventos que você participa
        % end
      </h2>

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
      <a class="btn btn-secondary" href="/"> Voltar</a>
    </div>
  </div>
</section>
