% rebase('layout.tpl', title='Detalhes do Pagamento')

<h2>Detalhes do Pagamento</h2>

% if payment:
    <ul>
        <li><strong>ID do Pagamento:</strong> {{payment.id}}</li>
        <li><strong>ID do Evento:</strong> {{payment.event_id}}</li>
        <li><strong>Email do Usuário:</strong> {{payment.user_email}}</li>
        <li><strong>Valor:</strong> R$ {{payment.amount}}</li>
        <li><strong>Status:</strong> {{payment.status}}</li>
    </ul>

    % if payment.status != 'paid':
        <form action="/payments/{{payment.id}}/confirm" method="POST">
            <button type="submit">Confirmar Pagamento</button>
        </form>
    % else:
        <p>Pagamento já foi confirmado.</p>
    % end
% else:
    <p>Pagamento não encontrado.</p>
% end
