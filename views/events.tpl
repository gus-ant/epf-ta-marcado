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
% if user:
  % if user.adm:
    <div class="container">
    <div style="margin-top: 20px; text-align: center; ">
      <a href="/events/create" class="btn" style="min-width: 400px">+ Crie um novo evento</a>
    </div>
  % end
% end

<!-- CRIA UMA FUNÇÃO PRA NÃO REPETIR AS GRADES-->
 % def render_event_section(title, events):
 <div class="container">
  <h2 class="section-title">{{title}}</h2>
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
            % if event.price == 0 or event.price == None:
              <p><strong>Entrada grátis</strong></p>
            % else:
              <p><strong>Preço:</strong> R$ {{'%.2f' % event.price}}</p>
            % end
            <a href="/events/{{event.id}}" class="btn">Ver Detalhes</a>
          </div>
        </div>
        % end
    </div>
  % else:
  <p>Nenhum evento disponível.</p>
  % end
 </div>
 % end
  
<!-- aqui faz as seções, pode adicionar mais sempre-->
 % render_event_section("🔥 Eventos mais populares!", top15_events)
 % render_event_section("📅 Eventos com data proxima", next_15_events)
 % render_event_section("Todos os proximos eventos", future_events)
 % render_event_section("📜 Eventos já encerrados", past_events)
</section>
