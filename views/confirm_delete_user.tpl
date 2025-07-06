% rebase('layout.tpl', title='Excluir Conta')

<div class="container">
  <h2>Excluir Conta</h2>
  <p>Esta ação é irreversível. Confirme sua senha e aguarde <strong id="countdown">5</strong> segundos antes de deletar.</p>

  % if error:
    <div class="alert alert-danger">{{error}}</div>
  % end

  <form method="POST" onsubmit="return confirmDelete();" class="form-group">
    <label for="password">Senha:</label>
    <input type="password" name="password" id="password" required>

<div>
  <br>
     <button type="submit" id="deleteBtn" class="btn btn-danger" disabled>Confirmar exclusão (5s)</button>
  </div>
  </form>
  
</div>

<script>
  let countdown = 5;
  const countdownElement = document.getElementById("countdown");
  const deleteBtn = document.getElementById("deleteBtn");

  const interval = setInterval(() => {
    countdown--;
    countdownElement.textContent = countdown;
    deleteBtn.textContent = `Confirmar exclusão (${countdown}s)`;

    if (countdown <= 0) {
      clearInterval(interval);
      deleteBtn.disabled = false;
      deleteBtn.textContent = "Confirmar exclusão";
    }
  }, 1000);

  function confirmDelete() {
    return confirm("Tem certeza que deseja excluir sua conta? Esta ação é permanente.");
  }
</script>
