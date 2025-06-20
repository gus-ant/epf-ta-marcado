from app import create_app

if __name__ == '__main__':
    app = create_app()
    app.run()
    
#LISTA TO-DO:

#terminar de adicionar comentarios na parte das views e app.py e config.py

#fazer verificação pra evitar email duplicado

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