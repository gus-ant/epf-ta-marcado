%rebase('layout', title='Login')

<section class="login-section">
  <div class="container login-card">
    <h2 class="section-title">🔐 Login</h2>

    % if error:
      <p class="alert">{{error}}</p>
    % end

    <form method="POST" class="form">
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" name="email" required placeholder="exemplo@email.com">
      </div>

      <div class="form-group">
        <label for="password">Senha:</label>
        <input type="password" name="password" required placeholder="Sua senha">
      </div>

      <button type="submit" class="btn">Entrar</button>
    </form>

    <p style="margin-top: 20px;">Não tem conta? <a href="/users/add">Cadastre-se aqui</a></p>
  </div>
</section>
