% rebase('layout', title='Detalhes do Pagamento')

<section class="payment-section">
  <div class="container">
    <div class="payment-card-centered">

      <h2 class="section-title" style="text-align: center;">💳 Detalhes do Pagamento</h2>

      % if payment:
        <ul class="payment-info">
          <li><strong>Nome do evento:</strong> {{payment.event_name}}</li>
          <li><strong>ID do Pagamento:</strong> {{payment.id}}</li>
          <li><strong>ID do Evento:</strong> {{payment.event_id}}</li>
          <li><strong>ID do Usuário:</strong> {{payment.user_id}}</li>
          % if payment.amount != None:
            <li><strong>Valor:</strong> R$ {{'%.2f' % payment.amount}}</li>
          % end
          <li>
            <strong>Status:</strong> 
            % if payment.status == 'paid':
              <span class="badge paid">✅ Pago</span>
            % elif payment.status == 'pending':
              <span class="badge pending">⏳ Pendente</span>
            % elif payment.status == 'refund_requested':
              <span class="badge refunding">🔄 Reembolso em andamento</span>
            % elif payment.status == 'refunded':
              <span class="badge refunded">💸 Reembolsado</span>
            % elif payment.status == 'cancelled':
              <span class="badge cancelled">❌ Cancelado</span> 
            % else:
              <span>{{payment.status}}</span>
            % end
          </li>
        </ul>

        <div class="payment-actions">

          % if payment.status == 'pending':
            <form action="/payments/{{payment.id}}/confirm" method="POST">
              <button type="submit" class="btn btn-success">✅ Confirmar Pagamento</button>
            </form>
            <form action="/payments/{{payment.id}}/cancel" method="POST">
              <button type="submit" class="btn btn-danger">❌ Cancelar Pagamento</button>
            </form>

          % elif payment.status == 'paid':
            <p class="alert alert-success">✅ Pagamento confirmado!</p>

            % if qr_code:
              <h3>Seu Ingresso (QR Code):</h3>
              <img src="data:image/png;base64,{{qr_code}}" alt="QR Code do ingresso" class="qr-code-img">
            % end

            <form action="/payments/{{payment.id}}/request_refund" method="POST">
              <button type="submit" class="btn btn-warning">🔁 Solicitar Reembolso</button>
            </form>

          % elif payment.status == 'refund_requested':
            <p>🔄 Seu reembolso está em andamento...</p>
            <form action="/payments/{{payment.id}}/confirm_refund" method="POST">
              <button type="submit" class="btn btn-info">💸 Confirmar Reembolso</button>
            </form>

          % elif payment.status == 'refunded':
            <p class="alert alert-info">💸 Este pagamento foi reembolsado com sucesso.</p>

          % elif payment.status == 'cancelled':
            <p class="alert alert-danger">❌ Este pagamento foi cancelado.</p>
          % end
        </div>

      % else:
        <p class="alert alert-warning">⚠️ Pagamento não encontrado.</p>
      % end

      <div class="form-actions" style="text-align: center; margin-top: 20px;">
        <a href="/user" class="btn btn-outline">← Voltar para o perfil</a>
      </div>

    </div>
  </div>
</section>
