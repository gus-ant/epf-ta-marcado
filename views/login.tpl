%rebase('layout', title='Eventos') 

<h2>Login</h2>
% if error:
<p style="color:red">{{error}}</p>
% end
<form method="POST">
    Email: <input type="email" name="email"><br>
    Senha: <input type="password" name="password"><br>
    <button type="submit">Entrar</button>
</form>
<p><a href="/users/add">Não tem conta? Cadastre-se</a></p>
