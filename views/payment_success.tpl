% rebase('layout.tpl', title='Pagamento atualizado')

<section class="payment-section">
  <div class="container payment-card">

    <h2 class="section-title">🔄 Nova atualização do pagamento!</h2>

    % if payment:
      <ul class="payment-info">
        <li><strong>ID do Pagamento:</strong> {{payment.id}}</li>
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

      <!-- Mensagem baseada no status -->
      % if payment.status == 'paid':
        <p class="alert alert-success">✅ Pagamento confirmado! Tá Marcado!📍.</p>
      % elif payment.status == 'pending':
        <p class="alert alert-warning">⏳ O pagamento ainda está pendente. Por favor, confirme ou cancele.</p>
      % elif payment.status == 'refund_requested':
        <p class="alert alert-info">🔄 Seu pedido de reembolso está sendo processado.</p>
      % elif payment.status == 'refunded':
        <p class="alert alert-success">💸 Reembolso concluído. O valor já está na sua conta.</p>
      % elif payment.status == 'cancelled':
        <p class="alert alert-danger">❌ Pagamento cancelado. Você não está mais no evento.</p>
      % end

    % else:
      <p class="alert">⚠️ Pagamento não encontrado.</p>
    % end

    <div class="form-actions" style="margin-top: 20px;">
      <a href="/user" class="btn">← Voltar ao Perfil</a>
      <a href="/events" class="btn btn-secondary">🎟️ Ver eventos</a>
    </div>

  </div>
</section>
