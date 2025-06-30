from app import create_app

if __name__ == '__main__':
    app = create_app()
    app.run()
    
#LISTA TO-DO:

#criar os outros tipos de erro em exceptions.py
#criar uma pagina de erro, pra quando der erro, o user ser redirecionado corretamente de volta pra home

#adicionar eventos no sistema:
# quando alguém comprar o ingresso, tirar uma vaga
#lista com todos os participantes no evento visivel pro adm
#-adm/events (pagina onde um adm pode ver os eventos que tem) 
#-na pagina do user, é possivel ver todos os eventos que participa
#-talvez adicionar outros tipos de ingresso (meia entrada e tals)
#ter likes no evento (cada user só pode dar 1 like)
#na pagina de eventos, a foto do evento ficar acima do nome

#login
#assim que criar conta, logar
#quando um user normal tentar fazer evento, aparecer o erro e voltar pra /home

#BUG FIX
#-não permitir mais que o user troque o email (ou quando ele trocar, todos os lugares onde aparece mudam tmb)

#criar a /home:
#-os usuarios vão direto pra /home ao abrir o programa
#- Temos que fazer a lógica (rota) do botão de search na página de eventos 

#criar e adicionar nossa logo no site 

#formatar o valor da entrada do evento pro formato R$

#metas pro projeto já pronto:
#-criptografar as senhas dos users no banco de dados JSON (muito importante)
#-verificar email
#-recuperar senha caso esqueca
#-usar likes como "algoritmo" pra mostrar os eventos com mais likes no topo do /home
# colocar um método para modificar as infos dos eventos
#--(podemos colocar como o clima vai estar no dia do evento)
#--(podemos colocar qrcode)
#quando um evento for apagado, mandar email pra todo mundo que se inscreveu E reembolsar


