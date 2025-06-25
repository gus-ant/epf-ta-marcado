% rebase('layout.tpl', title='Pagamento Concluído')

<h2>Pagamento realizado com sucesso!</h2>
<p>ID do pagamento: {{payment.id}}</p>
<p>Status: {{payment.status}}</p>
<a href="/events">Voltar aos eventos</a>
