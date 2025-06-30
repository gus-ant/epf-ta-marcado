% rebase('layout', title='Formulário Usuário')
<!-- entra na parte do !base em layout.tpl-->

<section class="form-section">
  <div class="container form-card">
    
    <h1 class="section-title">
      {{'✏️ Editar Usuário' if user else ' Cadastro de Usuário'}}
    </h1>

    <!-- mensagens de erro -->
    % if error:
      <p class="alert">{{error}}</p>
    % end

    % if defined('error') and error:
      <div class="alert">
        <p><strong>Erro:</strong> {{error}}</p>
      </div>
    % end

    <!-- formulário de cadastro/edição -->
    <form action="{{action}}" method="post" class="form">

      <!-- parte do nome -->
      <div class="form-group">
        <label for="name">Nome Completo:</label>
        <input type="text" id="name" name="name" required 
               value="{{user.name if user else ''}}" placeholder="Seu nome completo">
      </div>

      <!-- parte do email -->
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required 
               value="{{user.email if user else ''}}" placeholder="email@exemplo.com">
      </div>

      <!-- parte da data de nascimento -->
      <div class="form-group">
        <label for="birthdate">Data de Nascimento:</label>
        <input type="date" id="birthdate" name="birthdate" required 
               value="{{user.birthdate if user else ''}}">
      </div>

      <!-- parte da senha -->
      <div class="form-group">
        <label for="password">Senha:</label>
        <input type="password" id="password" name="password" minlength="8"
               placeholder="{{ 'Digite nova senha (opcional)' if user else 'Crie uma senha' }}"
               {{ "" if user else "required" }}>
        <small>Mínimo de 8 caracteres</small>
      </div>

      <!-- confirmação da senha -->
      <div class="form-group">
        <label for="password_confirm">Confirme a senha:</label>
        <input type="password" id="password_confirm" name="password_confirm" minlength="8"
               placeholder="{{ 'Confirme nova senha' if user else 'Confirme a senha' }}"
               {{ "" if user else "required" }}>
        <small>Mínimo de 8 caracteres</small>
      </div>

      <!-- parte do adm (só aparece no cadastro) -->
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
      <div class="form-actions">
        <button type="submit" class="btn">Salvar</button>
        <a href="/users" class="btn btn-secondary">Voltar</a>
      </div>

    </form>
  </div>
</section>
