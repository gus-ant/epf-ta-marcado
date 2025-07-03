%rebase('layout', title='Meus Pagamentos')

<section class="section">
  <div class="container">
    <h2 class="section-title">Meus Pagamentos</h2>

    % if payments:
      <table class="table">
        <thead>
          <tr>
            <th>Evento</th>
            <th>Valor</th>
            <th>Status</th>
            <th>QR Code</th>
          </tr>
        </thead>
        <tbody>
          % for payment in payments:
            <tr>
              <td>{{payment.event_name}}</td>
              <td>R$ {{'%.2f' % payment.amount}}</td>
              <td>
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
              </td>
              <td>
                % if payment.status == 'paid':
                  <a href="/payments/{{payment.id}}" class="btn" style="background-color: green; color: white;">Ver QR Code</a>
                % elif payment.status == 'pending':
                  <a href="/payments/{{payment.id}}" class="btn" style="background-color: darkorange; color: white;">Resolver pagamento</a>
                % elif payment.status == 'refund_requested':
                  <a href="/payments/{{payment.id}}" class="btn" style="background-color: blue; color: white;">Resolver reembolso</a>
                % else:
                  <span style="color: red;">Indisponível</span>
                % end
              </td>
            </tr>
          % end
        </tbody>
      </table>
    % else:
      <p class="muted">Você ainda não realizou nenhum pagamento.</p>
    % end
    <div style="margin-top: 20px;">
      <a class="btn btn-secondary" href="/user">Voltar ao Perfil</a>
    </div>
  </div>
</section>