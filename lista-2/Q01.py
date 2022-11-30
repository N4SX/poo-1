def tamString(s):

    a = 0

    for x in s:

        a += 1

    return a

palavra = input('Digite uma palavra:')
tamanho = tamString(palavra)
print('Quantidade de letras nessa palavra = {}'.format(tamanho))