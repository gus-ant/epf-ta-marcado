from app import create_app

if __name__ == '__main__':
    app = create_app()
    app.run()
    
#LISTA TO-DO:

#checar o que acontece quando deleta conta
#{
#rever as coisas que puxam user por email e trocar pra puxar por ID 
# se um adm deleta conta, eventos dele somem e as pessoas que tavam com pagamento pendente, cancelar, pago, reembolso pendente SÓ para eventos do futuro
#}

#COMEÇAR O README


#TEMOS QUE MUDAR ONDE PUXA POR EMAIL PRA PUXAR POR ID (explicação):
#- quando puxa por email, e se o user fizer a conta, apagar e fizer outra conta com o mesmo email, algumas infos podem ser puxadas do email antigo
#- o user pode só trocar o email
#- mas o id é sempre atualizado MESMO SE APAGAR A CONTA E FIZER OUTRA o id nunca vai ser o mesmo, o que garante sempre puxar o certo

#adicionar eventos no sistema:
#adicionar opção do dono excluir o evento (quando excluir o evento, aparecer pros users a opção de reembolso pendente pros que ja pagaram, pros que ainda não, cancelled, se for de graça, reembolsado)

#BUG FIX
#-não permitir mais que o user troque o email (ou quando ele trocar, todos os lugares onde aparece mudam tmb)
#--colocar uma confirmação de email (igual tem pra senha)
#-avisar na hora de fazer evento que não dá pra mudar as coisas do evento, explicar o pq

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