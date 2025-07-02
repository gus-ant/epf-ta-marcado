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
    <form action="/payments/{{payment.id}}/confirm" method="POST">
        <button type="submit">Confirmar Pagamento</button>
    </form>
    % else:
        <p>✅ Pagamento confirmado!</p>
    
        % if qr_code:
            <h3>Seu Ingresso (QR Code):</h3>
            <img src="{{qr_code}}" alt="QR Code do Ingresso">
        % end
    % end

    % if qr_code:
    <img src="data:image/png;base64,{{qr_code}}" alt="QR Code do ingresso">
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
