def AddNovoNome():

    nome = input('Nome: ')
    return nome.upper()

def AddNovoTelefone():

    telefone = input('Telefone: ')
    return telefone

def DelTelefone(dic):

    nome = input('Nome: ').upper()
    if nome in dic:

        telefone = input('Telefone: ')
        if telefone in dic[nome]:

            if(len(dic[nome])==1):

                del dic[nome]
            else:

                dic[nome].remove(telefone)
    return dic

def excluirNome(dic):

    nome = input('Nome que deseja deletar da agenda: ').upper()
    del dic[nome]
    return dic

def ConsultTelefone(dic):

    print('{} AGENDA {}'.format('=' * 4, '=' * 4))
    for chave, valor in dic.items():

        print(chave, valor)

dic = {}

while True:

    op = int(input('1.Adicionar novo nome\n2.Adicionar telefone\n3.Deletar telefone\n4.Deletar nome\n5.Consultar telefone\n'))

    if(op==1):

        dic.update({AddNovoNome(): []})
    elif(op==2):

        nome = input('Nome na agenda para adicionar telefone: ').upper()
        if(nome in dic):

            telefone = input('Telefone: ')
            dic[nome].append(telefone)
        else:

            cond = int(
                input('Nome não existe na agenda, deseja adicionar? <1> sim <outro valor> nao'))
            if(cond==1):

                dic.update({AddNovoNome(): []})
    elif(op==3):

        dic = DelTelefone(dic)
    elif(op==4):

        dic = excluirNome(dic)
    elif(op==5):

        ConsultTelefone(dic)
    else:

        break