% rebase('layout', title='Detalhes do Pagamento')

<section class="payment-section">
  <div class="container payment-card">
    
    <h2 class="section-title">💳 Detalhes do Pagamento</h2>

    % if payment:
      <ul class="payment-info">
        <li><strong>ID do Pagamento:</strong> {{payment.id}}</li>
        <li><strong>ID do Evento:</strong> {{payment.event_id}}</li>
        <li><strong>Email do Usuário:</strong> {{payment.user_email}}</li>
        <li><strong>Valor:</strong> R$ {{payment.amount}}</li>
        <li>
          <strong>Status:</strong> 
          <span class="badge {{'paid' if payment.status == 'paid' else 'pending'}}">
            {{'Pago' if payment.status == 'paid' else 'Pendente'}}
          </span>
        </li>
      </ul>

      % if payment.status != 'paid':
        <form action="/payments/{{payment.id}}/confirm" method="POST" class="form-actions">
        
          <button type="submit" class="btn"> Confirmar Pagamento</button>
        </form>
      % else:
        <p class="success-msg">✔️ Pagamento já foi confirmado.</p>
      % end

    % else:
      <p class="alert">⚠️ Pagamento não encontrado.</p>
    % end
    </br>
    <div class="form-actions">
      <a href="/events" class="btn ">← Voltar para eventos</a>
    </div>

  </div>
</section>
