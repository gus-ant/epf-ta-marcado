from app import create_app

if __name__ == '__main__':
    app = create_app()
    app.run()
    
#LISTA TO-DO:

#terminar de adicionar comentarios na parte das views e app.py e config.py

#criar os outros tipos de erro em exceptions.py
#criar uma pagina de erro, pra quando der erro, o user ser redirecionado corretamente de volta pra home

#adicionar eventos no sistema:
#adicionar descrição no evento (esqueci)
#event_controller
#events.tpl (pagina onde um adm pode ver os eventos que tem)
#na pagina do user, é possivel ver todos os eventos que participa
#ou o user vai ter uma lista com todos os seus eventos, ou puxar por email
#--(podemos colocar como o clima vai estar no dia do evento)
#--(podemos colocar qrcode)
#talver adicionar uma capa pro evento 
#no event_service fazer um edit_event
#talvez adicionar outros tipos de engresso(meia entrada e tals)

#BUG FIX
#-na parte de apagar user, lembrar de apagar todos os eventos que ele tem
#-ao apagar um evento, todo mundo inscrito sai do evento
#-quando um user for apagado, ele sai dos eventos e abre vaga


#criar a /home:
#-os usuarios vão direto pra /home ao abrir o programa

#o usuario que for adm ficar marcado com uma estrela 

#criar e adicionar nossa logo no site 
#titulo do site ser o nosso

#primeiro focar no python/html dps no css, quando tudo já funcionar, focar no CSS

#metas pro projeto já pronto:
#-criptografar as senhas dos users no banco de dados JSON