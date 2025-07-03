% rebase('layout', title='Detalhes do Pagamento')

<section class="payment-section">
  <div class="container payment-card">
    
    <h2 class="section-title">💳 Detalhes do Pagamento</h2>

    % if payment:
      <ul class="payment-info">
        <li><strong>Nome do evento:</strong> {{payment.event_name}}</li>
        <li><strong>ID do Pagamento:</strong> {{payment.id}}</li>
        <li><strong>ID do Evento:</strong> {{payment.event_id}}</li>
        <li><strong>Email do Usuário:</strong> {{payment.user_email}}</li>
        <li><strong>Valor:</strong> R$ {{payment.amount}}</li>
        <li>
          <strong>Status:</strong> 
          % if payment.status == 'paid':
            <span style="color: green;">✅ Pago</span>
          % elif payment.status == 'pending':
            <span style="color: orange;">⏳ Pendente</span>
          % elif payment.status == 'refund_requested':
            <span style="color: darkblue;">🔄 Reembolso em andamento</span>
          % elif payment.status == 'refunded':
            <span style="color: red;">💸 Reembolsado</span>
          % elif payment.status == 'cancelled':
            <span style="color: red;">❌ Cancelado</span> 
          % else:
            <span>{{payment.status}}</span>
          % end
        </li>
      </ul>

      <!--as diferentes açoes dependendo do estado do pagamento-->

      % if payment.status == 'pending':
    <form action="/payments/{{payment.id}}/confirm" method="POST">
        <button type="submit" class="btn" style="background-color: green; color: white;">✅ Confirmar Pagamento</button>
    </form>
    <form action="/payments/{{payment.id}}/cancel" method="POST">
      <button type="submit" class="btn" style="background-color: red; color: white;">❌ Cancelar Pagamento</button>
    </form>

      % elif payment.status == 'paid':
      <p>✅ Pagamento confirmado!</p>
        % if qr_code:
            <h3>Seu Ingresso (QR Code):</h3>
            <img src="data:image/png;base64,{{qr_code}}" alt="QR Code do ingresso">
        % end
        <form action="/payments/{{payment.id}}/request_refund" method="POST" style="margin-top: 10px;">
          <button type="submit" class="btn" style="background-color: orange; color: white;">🔁 Solicitar Reembolso</button>
        </form>

      % elif payment.status == 'refund_requested':
        <p>🔄 Seu reembolso está em andamento...</p>
        <form action="/payments/{{payment.id}}/confirm_refund" method="POST">
          <button type="submit" class="btn" style="background-color: blue; color: white;">💸 Confirmar Reembolso</button>
        </form>

      % elif payment.status == 'refunded':
        <p>💸 Este pagamento foi reembolsado com sucesso.</p>

      % elif payment.status == 'cancelled':
        <p>❌ Este pagamento foi cancelado.</p>
      % end
    % else:
      <p class="alert">⚠️ Pagamento não encontrado.</p>
    % end
    </br>
    <div class="form-actions">
      <a href="/user" class="btn ">← Voltar para o perfil</a>
    </div>

  </div>
</section>
