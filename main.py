from app import create_app

if __name__ == '__main__':
    app = create_app()
    app.run()
    
#LISTA TO-DO:

#terminar de adicionar comentarios na parte das views e app.py e config.py

#criar os outros tipos de erro em exceptions.py
#criar uma pagina de erro, pra quando der erro, o user ser redirecionado corretamente de volta pra home

#adicionar eventos no sistema:
#lista com todos os participantes no evento, usar email dos participantes (melhor do que id)
#-events.tpl (pagina onde um adm pode ver os eventos que tem) 👍
#-na pagina do user, é possivel ver todos os eventos que participa
#-ou o user vai ter uma lista com todos os seus eventos, ou puxar por email
#--(podemos colocar como o clima vai estar no dia do evento)
#--(podemos colocar qrcode)
#-poder adicionar uma capa pro evento (Acho importante, mas vai ter que mexer com imagem)
#-no event_service fazer um edit_event
#-talvez adicionar outros tipos de ingresso(meia entrada e tals)
#ter likes no evento (cada user só pode dar 1 like)

#login
#-um usuario pode escolher logar ou criar conta
#-uma vez logado, vai pra /home

#BUG FIX
#-na parte de apagar user, lembrar de apagar todos os eventos que ele tem
#-ao apagar um evento, todo mundo inscrito sai do evento (lista no evento)
#-quando um user for apagado, ele sai dos eventos e abre vaga
#-quando um adm for apagado todos os eventos dele somem
#-não permitir mais que o user troque o email


#criar a /home:
#-os usuarios vão direto pra /home ao abrir o programa

#criar e adicionar nossa logo no site 
#titulo do site ser o nosso

#primeiro focar no python/html dps no css, quando tudo já funcionar, focar no CSS

#metas pro projeto já pronto:
#-criptografar as senhas dos users no banco de dados JSON (muito importante)
#-usar likes como "algoritmo" pra mostrar os eventos com mais likes no topo do /home