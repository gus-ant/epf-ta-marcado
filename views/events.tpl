%rebase('layout', title='Eventos')


<div class="hero-banner">
  <div class="hero-content">
    <h1>Encontre o Evento Perfeito</h1>
    <p>Busque por nome, local ou palavra-chave</p>
    <form action="/events/search" method="get" class="search-bar">
      <input type="text" name="q" placeholder="Pesquisar eventos..." required>
      <button type="submit" class="btn">Buscar</button>
    </form>
  </div>
</div>

  <div class="container">

  
    <h2 class="section-title">Eventos Disponíveis</h2>

    % if events:
      <div class="events-grid">
        % for event in events:
          <div class="card">
            % if event.cover:
              <img src="/static/uploads/event_covers/{{event.cover}}" alt="Capa do evento {{event.name}}">
            % else:
              <img src="/static/img/BottleLogo.png" alt="Evento sem imagem">
            % end

            <div class="card-body">
              <h3><a href="/events/{{event.id}}">{{event.name}}</a></h3>
              <p><strong>Local:</strong> {{event.local}}</p>

              % if event.price == 0:
                <p><strong>Entrada grátis</strong></p>
              % else:
                <p><strong>Preço:</strong> R$ {{event.price}}</p>
              % end

              <a href="/events/{{event.id}}" class="btn">Ver Detalhes</a>
            </div>
          </div>
        % end
      </div>
    % else:
      <p>Nenhum evento disponível no momento.</p>
    % end

    <div style="margin-top: 40px;">
      <a href="/events/create" class="btn">+ Criar novo evento</a>
    </div>
  </div>
</section>
