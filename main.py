from app import create_app

if __name__ == '__main__':
    app = create_app()
    app.run()
    
#LISTA TO-DO:

#adicionar no user uma lista com todos os pagamentos do user

#criar os outros tipos de erro em exceptions.py

#fazer a pesquisa existir

#fazer:
#botão de sair do evento
#fazer o botão de cancelar pagamento 
#SÓ COLOCAR O USER NO EVENTO QUANDO CONFIRMAR PAGAMENTO
#adm poder ver todos os pagamentos dos eventos dele

#CRIEI UM ADM, FUI NA PAGINA DE EVENTOS E NÃO APARECEU A OPÇÃO DE FAZER EVENTO (SÓ QUANDO DERRUBA E VOLTA O SERVER)
#TEMOS QUE MUDAR ONDE PUXA POR EMAIL PRA PUXAR POR ID (explicação):
#- quando puxa por email, e se o user fizer a conta, apagar e fizer outra conta com o mesmo email, algumas infos podem ser puxadas do email antigo
#- mas o id é sempre atualizado MESMO SE APAGAR A CONTA E FIZER OUTRA o id nunca vai ser o mesmo

#adicionar eventos no sistema:
#adicionar opção de sair do evento
#adicionar opção do dono excluir o evento (quando excluir o evento, aparecer pros users a opção de reembolso pendente pros que ja pagaram, pros que ainda não, cancelled)
#-talvez adicionar outros tipos de ingresso (meia entrada e tals)
#ter likes no evento (cada user só pode dar 1 like)

#BUG FIX
#-não permitir mais que o user troque o email (ou quando ele trocar, todos os lugares onde aparece mudam tmb)
#--colocar uma confirmação de email (igual tem pra senha)
#-avisar na hora de fazer evento que não dá pra mudar as coisas do evento, explicar o pq

#formatar o valor da entrada do evento pro formato R$

#metas pro projeto já pronto:
#-fazer o readme e rever as metas do projeto no github do prof
#-criptografar as senhas dos users no banco de dados JSON (muito importante)
#-verificar email
#-recuperar senha caso esqueca
#-usar likes como "algoritmo" pra mostrar os eventos com mais likes no topo do /home
#--(podemos colocar como o clima vai estar no dia do evento)
#quando um evento for apagado, mandar email pra todo mundo que se inscreveu E reembolsar


