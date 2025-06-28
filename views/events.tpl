%rebase('layout', title='Eventos')

<section class="section">

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

    % if eventos:
      <div class="events-grid">
        % for evento in eventos:
          <div class="card">
            % if evento.cover:
              <img src="/static/uploads/event_covers/{{evento.cover}}" alt="Capa do evento {{evento.name}}">
            % else:
              <img src="/static/img/BottleLogo.png" alt="Evento sem imagem">
            % end

            <div class="card-body">
              <h3><a href="/events/{{evento.id}}">{{evento.name}}</a></h3>
              <p><strong>Local:</strong> {{evento.local}}</p>

              % if evento.price == 0:
                <p><strong>Entrada grátis</strong></p>
              % else:
                <p><strong>Preço:</strong> R$ {{evento.price}}</p>
              % end

              <a href="/events/{{evento.id}}" class="btn">Ver Detalhes</a>
            </div>
          </div>
        % end
      </div>
    % else:
      <p>Nenhum evento disponível no momento.</p>
    % end

    <div style="margin-top: 80px;">
      <a href="/events/create" class="btn">+ Criar novo evento</a>
    </div>
  </div>
</section>
