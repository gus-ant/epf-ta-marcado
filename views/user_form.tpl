% rebase('layout', title='Formulário Usuário')

<section class="form-section">
  <div class="container form-card">

    <h1 class="section-title">
      {{'✏️ Editar Usuário' if user else ' Cadastro de Usuário'}}
    </h1>

    % if error:
      <p class="alert">{{error}}</p>
    % end

    <!-- Form principal -->
    <form action="{{action}}" method="post" class="form">

      <!-- campos do form -->
      <div class="form-group">
        <label for="name">Nome Completo:</label>
        <input type="text" id="name" name="name" required
               value="{{user.name if user else ''}}" placeholder="Seu nome completo">
      </div>

      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required
               value="{{user.email if user else ''}}" placeholder="email@exemplo.com">
      </div>

      <div class="form-group">
        <label for="birthdate">Data de Nascimento:</label>
        <input type="date" id="birthdate" name="birthdate" required
               value="{{user.birthdate if user else ''}}">
      </div>

      <div class="form-group">
        <label for="password">Senha:</label>
        <input type="password" id="password" name="password" minlength="8"
               placeholder="{{ 'Digite nova senha (opcional)' if user else 'Crie uma senha' }}"
               {{ "" if user else "required" }}>
        <small>Mínimo de 8 caracteres</small>
      </div>

      <div class="form-group">
        <label for="password_confirm">Confirme a senha:</label>
        <input type="password" id="password_confirm" name="password_confirm" minlength="8"
               placeholder="{{ 'Confirme nova senha' if user else 'Confirme a senha' }}"
               {{ "" if user else "required" }}>
        <small>Mínimo de 8 caracteres</small>
      </div>

      % if not user:
      <div class="form-group checkbox-group">
        <label>
          <input type="checkbox" name="adm" {{'checked' if user and user.adm else ''}}>
          <span class="checkmark"></span>
          Adm (pode criar eventos)
        </label>
      </div>
      % end

      <!-- botões -->
      <div class="form-actions" style="display: flex; gap: 10px; margin-top: 20px;">
        <button type="submit" class="btn" style="flex: 1; color: white; background-color: blue;">Salvar</button>
        <a href="/users" class="btn btn-secondary" style="flex: 1; display: flex; justify-content: center; align-items: center; text-decoration: none;">Voltar</a>
      </div>
    </form>

    % if user:
    <!-- Form de deletar fora do form principal -->
    <div style="margin-top: 10px;">
      <form action="/users/delete/{{user.id}}" method="post" onsubmit="return confirm('Tem certeza que deseja excluir esta conta? Esta ação não pode ser desfeita.')" style="width: 100%;">
        <button type="submit" class="btn btn-secondary" style="width: 100%; color: white; background-color: red;">
          Deletar conta
        </button>
      </form>
    </div>
    % end
    </form>

  </div>
</section>