% rebase('layout', title='Formulário Usuário')
 <!-- entra na parte do !base em layout.tpl-->

<section class="form-section">
    <h1>{{'Editar Usuário' if user else 'Adicionar Usuário'}}</h1>
    
    % if error:
        <p style="color: red;">Erro: {{error}}</p>
    % end

    % if defined('error') and error:
        <div class="error-message">
            <p><strong>Erro:</strong> {{error}}</p>
        </div>
    % end

    <form action="{{action}}" method="post" class="form-container">

        <!-- parte do nome-->
        <div class="form-group">
            <label for="name">Nome Completo:</label>
            <input type="text" id="name" name="name" required 
                   value="{{user.name if user else ''}}">
        </div>
        
        <!-- parte do email-->
        <div class="form-group">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required 
                   value="{{user.email if user else ''}}">
        </div>
        
        <!-- parte da data de nascimento-->
        <div class="form-group">
            <label for="birthdate">Data de Nascimento:</label>
            <input type="date" id="birthdate" name="birthdate" required 
                   value="{{user.birthdate if user else ''}}">
        </div>
        
        <!-- parte da senha-->
        <div class = "form-group"> 
            <label for="password">Senha:</label>
            <input type="password" id="password" name="password" minlength="8"
                placeholder='{{ "Digite nova senha (opcional)" if user else "" }}'
                {{ "" if user else "required" }}>
            <small>Mínimo de 8 caracteres</small>
        </div>

        <div class = "form-group">
            <label for="password_confirm">Confirme a senha:</label>
            <input type="password" id="password_confirm" name="password_confirm" minlength="8"
                placeholder='{{ "Digite nova senha (opcional)" if user else "" }}'
                {{ "" if user else "required" }}>
            <small>Mínimo de 8 caracteres</small>
        </div>

        <!-- parte do adm-->
         <div class = "form-group checkbox-group">
            <label>
                <input type="checkbox" name="adm"
                    {{'checked' if user and user.adm else''}}>
                <span class="checkmark"></span>
                Adm (pode criar eventos)
            </label>
         </div>


        <div class="form-actions">
            <button type="submit" class="btn-submit">Salvar</button>
            <a href="/users" class="btn-cancel">Voltar</a>
        </div>
    </form>
</section>