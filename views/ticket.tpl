% rebase('layout.tpl', title='Ingresso')

<div class="modal">
    <h2>{{dados['evento']}}</h2>
    <p>
        <strong>Data:</strong> {{dados['data']}} às {{dados['hora']}}<br>
        <strong>Local:</strong> {{dados['local']}}<br>
        <strong>Ingresso:</strong> {{dados['tipo_ingresso']}}<br>
        <strong>Quantidade:</strong> {{dados['quantidade']}}<br>
        <strong>Total:</strong> R$ {{'%.2f' % dados['valor_total']}}<br>
    </p>

    <img src="data:image/png;base64,{{qr}}" alt="QR Code do Ingresso" style="width: 200px;">
</div>
