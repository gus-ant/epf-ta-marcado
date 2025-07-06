from app import create_app

if __name__ == '__main__':
    app = create_app()
    app.run()
    
#LISTA TO-DO:

#checar o que acontece quando deleta conta
#{
#rever as coisas que puxam user por email e trocar pra puxar por ID 🧧 (lista de participantes do evento e id do pagamento do user)
#adm conseguir apagar conta (apagar todos os eventos dele) 
#adicionar opção do dono excluir o evento
#-(quando excluir o evento, aparecer pros users a opção de reembolso pendente pros que ja pagaram, pros que ainda não, cancelled, se for de graça, reembolsado)
#}

#TEMOS QUE MUDAR ONDE PUXA POR EMAIL PRA PUXAR POR ID (explicação):
#- quando puxa por email, e se o user fizer a conta, apagar e fizer outra conta com o mesmo email, algumas infos podem ser puxadas do email antigo
#- o user pode só trocar o email
#- mas o id é sempre atualizado MESMO SE APAGAR A CONTA E FIZER OUTRA o id nunca vai ser o mesmo, o que garante sempre puxar o certo

#metas pro projeto já pronto:
#-fazer o issues
#-fazer o readme e rever as metas do projeto no github do prof
#-apagar o banco de dados inteiro e testar tudo que a gente vai apresentar META FINAL!!!