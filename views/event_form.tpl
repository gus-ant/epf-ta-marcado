% rebase('layout', title='Formulário de Evento')

<section class="form-section">
  <div class="container form-card">
    
    <h1 class="section-title">
    % if event:
        Editar Evento
    % else:
        🗓️ Criar Novo Evento
    
    </h1>

    % if error:
      <div class="alert">
        <p><strong>Erro:</strong> {{error}}</p>
      </div>
    % end

    <form action="{{action}}" method="post" enctype="multipart/form-data" class="form">

      <!-- Título do evento -->
      <div class="form-group">
        <label for="name">Nome do Evento:</label>
        <input type="text" id="name" name="name" required 
               value="{{event.name if event else ''}}" placeholder="Ex: Festa de Aniversário">
      </div>

      <!-- Local do evento -->
      <div class="form-group">
        <label for="local">Local:</label>
        <input type="text" id="local" name="local" required 
               value="{{event.local if event else ''}}" placeholder="Ex: Salão de festas, Brasília - DF">
      </div>

      <!-- Data -->
      <div class="form-group">
        <label for="date">Data:</label>
        <input type="date" id="date" name="date" required 
               value="{{event.date if event else ''}}">
      </div>

      <!-- Hora -->
      <div class="form-group">
        <label for="time">Horário:</label>
        <input type="time" id="time" name="time" required 
               value="{{event.time if event else ''}}">
      </div>

      <!-- Preço -->
      <div class="form-group">
        <label for="price">Preço (R$):</label>
        <input type="number" step="0.01" id="price" name="price" min="0" required 
               value="{{event.price if event else 0}}">
        <small>Coloque 0 para evento gratuito</small>
      </div>

      <!-- Capacidade -->
      <div class="form-group">
        <label for="max_capacity">Capacidade Máxima:</label>
        <input type="number" id="max_capacity" name="max_capacity" min="1" required 
               value="{{event.max_capacity if event else 1}}">
      </div>

      <!-- Descrição -->
      <div class="form-group">
        <label for="description">Descrição:</label>
        <textarea id="description" name="description" rows="4" placeholder="Descrição do evento...">{{event.description if event else ''}}</textarea>
      </div>

      <!-- Capa -->
      <div class="form-group">
        <label for="cover">Imagem de Capa:</label>
        <input type="file" id="cover" name="cover" accept="image/*">
        % if event and event.cover:
          <p>Imagem atual:</p>
          <img src="/static/uploads/event_covers/{{event.cover}}" style="max-width: 200px; border-radius: 10px;">
        % end
      </div>

      <!-- Ações -->
      <div class="form-actions">
        <button type="submit" class="btn">{{ 'Salvar Alterações' if event else 'Criar Evento' }}</button>
        <a href="/events" class="btn btn-secondary">Cancelar</a>
      </div>
    </form>
  </div>
</section>
