def media(x):

    soma = 0
    for i in x:

        soma += i
    return soma/len(x)


dicionario = {}
while True:

    nome = input('Nome: ')
    notas = [0] * 2
    for i in range(2):

        print('Nota {}: '.format(i+1), end=" ")
        notas[i] = float(input())

    dicionario.update({nome.upper(): notas})
    x = 0
    if(x != 1):

        break

while True:

    busca = input('Nome do aluno: ')
    busca = busca.upper()
    if busca in dicionario:

        print('Aluno: {}\nNotas: {}\nMedia: {}'.format(busca, dicionario[busca], media(dicionario[busca])))
    else:

        print('Aluno não encontrado ')
    x = int(input('<1> Digitar novamente <outro valor> sair: '))
    if x != 1:

        break