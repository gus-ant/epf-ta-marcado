from app import create_app

if __name__ == '__main__':
    app = create_app()
    app.run()
    
#LISTA TO-DO:

#fazer:
#adm poder ver todos os pagamentos dos eventos dele


#fazer as coisas pra eventos expirados:
# não aparecer nos top 15 nem no todos os eventos
# quando for ver details aparecer na data EXPIRADO em vermelho ao lado da data
# não poder pedir reembolso do pagamento

#na /events fazer nessa ordem:
# top 15 eventos com mais pessoas inscritas (vai entrar no lugar do like)
# top 15 eventos mais proximos (data)
# todos os eventos
# eventos expirados

#checar o que acontece quando deleta conta
#{
#avisar quando for deletar que ainda tem pagamentos possiveis em andamento
#fazer uma pagina pra confirmar o delete, onde o user tem que informar a senha e confirmar (botão com timer)
#ver se o user sai de todos os eventos
#rever as coisas que puxam user por email e trocar pra puxar por ID 
#}
#COLOCAR O STYLE NO STYLE.CSS EM VEZ DE LAYOUT
#COMEÇAR O README


#TEMOS QUE MUDAR ONDE PUXA POR EMAIL PRA PUXAR POR ID (explicação):
#- quando puxa por email, e se o user fizer a conta, apagar e fizer outra conta com o mesmo email, algumas infos podem ser puxadas do email antigo
#- mas o id é sempre atualizado MESMO SE APAGAR A CONTA E FIZER OUTRA o id nunca vai ser o mesmo, o que garante sempre puxar o certo

#adicionar eventos no sistema:
#adicionar opção do dono excluir o evento (quando excluir o evento, aparecer pros users a opção de reembolso pendente pros que ja pagaram, pros que ainda não, cancelled, se for de graça, reembolsado)

#BUG FIX
#-não permitir mais que o user troque o email (ou quando ele trocar, todos os lugares onde aparece mudam tmb)
#--colocar uma confirmação de email (igual tem pra senha)
#-avisar na hora de fazer evento que não dá pra mudar as coisas do evento, explicar o pq

#formatar o valor da entrada do evento pro formato R$

#metas pro projeto já pronto:
#-talvez adicionar outros tipos de ingresso (meia entrada e tals)
#-fazer o readme e rever as metas do projeto no github do prof
#-criptografar as senhas dos users no banco de dados JSON (muito importante)
#-verificar email
#-recuperar senha caso esqueca
#-usar likes como "algoritmo" pra mostrar os eventos com mais likes no topo do /home
#--(podemos colocar como o clima vai estar no dia do evento)
#quando um evento for apagado, mandar email pra todo mundo que se inscreveu E reembolsar
#ter likes no evento (cada user só pode dar 1 like)


