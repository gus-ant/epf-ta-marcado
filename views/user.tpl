%rebase('layout', title='Perfil')

<section class="profile">
    <h1>Perfil do {{ user.name }}</h1>

    <div class="profile-info">
        <p><strong>Nome:</strong> {{ user.name }}</p>
        <p><strong>Email:</strong> {{user.email }}</p>
        <p><strong>Data de nascimento:</strong> {{ user.birthdate }}</p>
        <p><strong>Senha:</strong> ********</p>
        <p><strong>Tipo de conta:</strong> {{ 'Adm' if user.adm else 'Comum' }}
        % if user.adm:
            <span title="Admin" style="color: gold; margin-right: 5px;">&#11088;</span></p>
        % end
    </div>

    <div class="profile-actions">
        <a class="btn-edit" href="/users/edit/{{user.id}}">Editar perfil</a>
        <a class="btn-back" href="/">Voltar</a>
    </div>
</section>