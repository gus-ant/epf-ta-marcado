%rebase('layout', title='Usuários')

<section class="section">
  <div class="container">
    <div class="section-header" style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px; margin-top: 24px;">
      <h2 class="section-title"><i class="fas fa-users"></i> Gestão de Usuários</h2>
      <a href="/users/add" class="btn">
        <i class="fas fa-plus"></i> Novo Usuário
      </a>
    </div>

    <div class="table-container">
      <table class="styled-table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Nome</th>
            <th>Email</th>
            <th>Data de Nascimento</th>
            <th>Ações</th>
          </tr>
        </thead>
        <tbody>
          % for u in users:
          <tr>
            <td>{{u.id}}</td>
            <td>{{u.name}}</td>
            <td><a href="mailto:{{u.email}}">{{u.email}}</a></td>
            <td>{{u.birthdate}}</td>
            <td class="actions">
              <a href="/users/edit/{{u.id}}" class="btn btn-sm btn-edit">
                <i class="fas fa-edit"></i> Editar
              </a>
              <form action="/users/delete/{{u.id}}" method="post" style="display:inline;" onsubmit="return confirm('Tem certeza que deseja excluir?')">
                <button type="submit" class="btn btn-sm btn-danger">
                  <i class="fas fa-trash-alt"></i> Excluir
                </button>
              </form>
            </td>
          </tr>
          % end
        </tbody>
      </table>
    </div>
  </div>
</section>
