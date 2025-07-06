from app import create_app

if __name__ == '__main__':
    app = create_app()
    app.run()
    
#LISTA TO-DO:
# ao apagar o user ele não sai mais do evento (eu criei entrei e apaguei sem dar refresh no server)
#checar o que acontece quando deleta conta
#{
#adm conseguir apagar conta (apagar todos os eventos dele) 🧧
#adicionar opção do dono excluir o evento 🧧
#-(quando excluir o evento, aparecer pros users a opção de reembolso pendente pros que ja pagaram, pros que ainda não, cancelled, se for de graça, reembolsado)
#}

#metas pro projeto já pronto:
#-fazer o issues
#-fazer o readme e rever as metas do projeto no github do prof
#-apagar o banco de dados inteiro e testar tudo que a gente vai apresentar META FINAL!!!