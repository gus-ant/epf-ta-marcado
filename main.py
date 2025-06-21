from app import create_app

if __name__ == '__main__':
    app = create_app()
    app.run()
    
#LISTA TO-DO:

#terminar de adicionar comentarios na parte das views e app.py e config.py

#criar os outros tipos de erro em exceptions.py
#criar uma pagina de erro, pra quando der erro, o user ser redirecionado corretamente de volta pra home

#adicionar eventos no sistema:
#-os eventos tem:
#--local
#--data (quando expira aparece um aviso e sai do sistema depois de uma semana)
#--lotação maxima
#--preço do evento
#--horario
#--(podemos colocar como o clima vai estar no dia do evento)
#--(podemos colocar qrcode)

#criar a /home:
#-os usuarios vão direto pra /home ao abrir o programa

#o usuario que for adm ficar marcado com uma estrela 

#criar e adicionar nossa logo no site 
#titulo do site ser o nosso

#primeiro focar no python/html dps no css, quando tudo já funcionar, focar no CSS

#metas pro projeto já pronto:
#-criptografar as senhas dos users no banco de dados JSON