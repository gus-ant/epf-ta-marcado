% rebase('layout.tpl', title='Pagamento')

<h2>Pagamento do Evento #{{pg.id_evento}}</h2>
<p>Valor a pagar: R$ {{pg.valor}}</p>

<form method="post">
    <label>Número do cartão (simulação):</label><br>
    <input type="text" name="cartao" required><br><br>
    <button type="submit">Confirmar Pagamento</button>
</form>
