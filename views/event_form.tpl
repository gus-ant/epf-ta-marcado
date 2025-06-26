%rebase('layout', title='Eventos') 

<body>
    <h1>Criar Evento</h1>

    % if error:
        <p style="color: red;">Erro: {{error}}</p>
    % end

    <form action="{{action}}" method="post" enctype="multipart/form-data">
        <label for="name">Nome do Evento:</label><br>
        <input type="text" id="name" name="name" required><br><br>

        <label for="local">Local:</label><br>
        <input type="text" id="local" name="local" required><br><br>

        <label for="date">Data:</label><br>
        <input type="date" id="date" name="date" required><br><br>

        <label for="time">Horário:</label><br>
        <input type="time" id="time" name="time" required><br><br>

        <label for="price">Preço (R$):</label><br>
        <input type="number" step="0.01" id="price" name="price" min="0" placeholder="0.00"><br><br>

        <label for="max_capacity">Capacidade Máxima:</label><br>
        <input type="number" id="max_capacity" name="max_capacity" required><br><br>

        <label for="description">Descrição:</label><br>
        <textarea type="text" id="description" name="description" rows="6" cols="45"></textarea>

        <label for="cover">Capa do evento:</label>
        <input type="file" id="cover" name="cover" accept="image/*"><br><br>

        <input type="submit" value="Criar Evento">
    </form>

    <p><a href="/events">Voltar para a lista de eventos</a></p>
</body>