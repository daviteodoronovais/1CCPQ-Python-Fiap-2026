listaEmail = ('langas@gmail.com', 'dungas@gmail.com', 'lingas@fiap.com.br', 'pinbas@xangaslungas.com.br')

for email in listaEmail:
    usuario, dominio = email.split('@')
    print(usuario, dominio)
#CONTINUAR...