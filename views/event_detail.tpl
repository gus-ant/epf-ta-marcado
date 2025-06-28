%rebase('layout', title=evento.name)

<section class="section">
  <div class="container">

    <!-- Card principal do evento -->
    <div class="event-detail-card">
      % if evento.cover:
        <img src="/static/uploads/event_covers/{{evento.cover}}" alt="Capa do evento {{evento.name}}">
      % else:
        <img src="/static/img/BottleLogo.png" alt="Evento sem imagem">
      % end

      <div class="event-info">
        <h2 class="section-title" style="margin-bottom: 12px;">{{evento.name}}</h2>

        <p><strong>Local:</strong> {{evento.local}}</p>
        <p><strong>Data:</strong> {{evento.date}} às {{evento.time}}</p>

        % if evento.price == 0:
          <p><strong>Entrada grátis</strong></p>
        % else:
          <p><strong>Preço:</strong> R$ {{evento.price}}</p>
        % end

        <p><strong>Capacidade:</strong> {{evento.current_capacity}} / {{evento.max_capacity}}</p>
        <p><strong>Descrição:</strong> {{evento.description}}</p>
        <p style="font-size: .9rem; color: var(--muted-text-color);">
          <strong>Email do criador:</strong> {{evento.owner_email}}
        </p>

        <form action="/events/{{evento.id}}/join" method="post" style="margin-top: 20px;">
          <button type="submit" class="btn">
            ❤️ Quero ir
          </button>
        </form>
      </div>
    </div>

  </div>
</section>
