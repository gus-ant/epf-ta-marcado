% rebase('layout.tpl', title='Pagamento Concluído')

<section class="payment-section">
  <div class="container payment-card">

    <h2 class="section-title">✅ Pagamento realizado com sucesso!</h2>

    % if payment:
      <ul class="payment-info">
        <li><strong>ID do Pagamento:</strong> {{payment.id}}</li>
        <li>
          <strong>Status:</strong> 
          <span class="badge {{'paid' if payment.status == 'paid' else 'pending'}}">
            {{'Pago' if payment.status == 'paid' else 'Pendente'}}
          </span>
        </li>
      </ul>
    % else:
      <p class="alert">⚠️ Pagamento não encontrado.</p>
    % end

    <div class="form-actions">
      <a href="/events" class="btn">← Voltar para eventos</a>
    </div>

  </div>
</section>
