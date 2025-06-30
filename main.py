from app import create_app

if __name__ == '__main__':
    app = create_app()
    app.run()
    
#LISTA TO-DO:

#criar os outros tipos de erro em exceptions.py

#adicionar eventos no sistema:
#adicionar opção de sair do evento
#adicionar opção do dono excluir o evento
#-talvez adicionar outros tipos de ingresso (meia entrada e tals)
#ter likes no evento (cada user só pode dar 1 like)

#login
#assim que criar conta, logar

#BUG FIX
#-não permitir mais que o user troque o email (ou quando ele trocar, todos os lugares onde aparece mudam tmb)
#--colocar uma confirmação de email (igual tem pra senha)
#-avisar na hora de fazer evento que não dá pra mudar as coisas do evento, explicar o pq

#criar a /home:
#/events é a home fds


#formatar o valor da entrada do evento pro formato R$

#metas pro projeto já pronto:
#-fazer o readme e rever as metas do projeto no github do prof
#-criptografar as senhas dos users no banco de dados JSON (muito importante)
#-verificar email
#-recuperar senha caso esqueca
#-usar likes como "algoritmo" pra mostrar os eventos com mais likes no topo do /home
# colocar um método para modificar as infos dos eventos
#--(podemos colocar como o clima vai estar no dia do evento)
#--(podemos colocar qrcode)
#quando um evento for apagado, mandar email pra todo mundo que se inscreveu E reembolsar


