%rebase('layout', title='Eventos') 

<h1>Criar Evento</h1>

% if error:
    <p style="color: red">{{error}}</p>

<form action="{{action}}" method="post">
    Nome: <input type="text" name="name"><br>
    Local: <input type="text" name="local"><br>
    Data: <input type="date" name="date"><br>
    Hora: <input type="time" name="time"><br>
    Preço: <input type="number" step="0.01" name="price"><br>
    Capacidade Máxima: <input type="number" name="max_capacity"><br>
    <input type="submit" value="Criar Evento">
</form>
