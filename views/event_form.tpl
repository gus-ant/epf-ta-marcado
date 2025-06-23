%rebase('layout', title='Eventos') 

<body>
    <h1>Criar Evento</h1>

    % if error:
        <p style="color: red;">Erro: {{error}}</p>
    % end

    <form action="{{action}}" method="post">
        <label for="name">Nome do Evento:</label><br>
        <input type="text" id="name" name="name" required><br><br>

        <label for="local">Local:</label><br>
        <input type="text" id="local" name="local" required><br><br>

        <label for="date">Data:</label><br>
        <input type="date" id="date" name="date" required><br><br>

        <label for="time">Horário:</label><br>
        <input type="time" id="time" name="time" required><br><br>

        <label for="price">Preço (R$):</label><br>
        <input type="number" step="0.01" id="price" name="price" required><br><br>

        <label for="max_capacity">Capacidade Máxima:</label><br>
        <input type="number" id="max_capacity" name="max_capacity" required><br><br>
        
        <label for="owner_email">Email do Criador:</label><br>
        <input type="text" id="owner_email" name="owner_email" required><br><br>
        <!-- deixar o owner_email automatico usando o user logado-->

        <label for="description">Descrição:</label><br>
        <textarea type="text" id="description" name="description" rows="6" cols="45"></textarea>

        <input type="submit" value="Criar Evento">
    </form>

    <p><a href="/events">Voltar para lista de eventos</a></p>
</body>