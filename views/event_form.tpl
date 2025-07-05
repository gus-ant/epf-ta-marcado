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
        <input type="text" id="name" name="name" minlength="3" maxlength="30" required 
               value="{{event.name if event else ''}}" placeholder="Ex: Festa de Aniversário">
      </div>

      % if error:
        <p style="color: red;">Erro: {{error}}</p>
      % end

      <!-- Local do evento -->
      <div class="form-group">
        <label for="local">Local:</label>
        <input type="text" id="local" name="local" minlength="3" maxlength="40" required 
               value="{{event.local if event else ''}}" placeholder="Ex: Salão de festas, Brasília - DF">
      </div>

      <!-- Data -->
      <!-- minimo, dia atual e maximo 10 anos no futuro-->
      <div class="form-group">
        <label for="date">Data:</label>
        <input type="date" id="date" name="date" required 
               value="{{event.date if event else ''}}"
               min="{{datetime.today().strftime('%Y-%m-%d')}}"
               max="{{(datetime.today() + timedelta(days=365*10)).strftime('%Y-%m-%d')}}">
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
        <input type="text"
              id="price"
              name="price"
              required
              inputmode="numeric"
              pattern="^R\$ ?\d{1,3}(\.\d{3})*(,\d{2})?$|^R\$ ?\d+(,\d{2})?$"
              title="Formato inválido. Use o formato R$ 0,00"
              oninvalid="this.setCustomValidity('Formato inválido. Ex: R$ 10,00')"
              oninput="this.setCustomValidity('')"
              value="{{ ('R$ %.2f' % event.price).replace('.', ',') if event and event.price != None else 'R$ 0,00' }}"
              placeholder="R$ 0,00">
        <small>deixe 0 para evento gratuito</small>
      </div>

      <!-- Capacidade -->
      <div class="form-group">
        <label for="max_capacity">Capacidade Máxima:</label>
        <input type="number" id="max_capacity" name="max_capacity" min="1" step="1" required 
               value="{{event.max_capacity if event else 1}}">
      </div>

      <!-- Descrição -->
      <div class="form-group">
        <label for="description">Descrição:</label>
        <textarea id="description" name="description" rows="4" maxlength="200" placeholder="Descrição do evento...">{{event.description if event else ''}}</textarea>
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
