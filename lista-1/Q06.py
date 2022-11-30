def primo(N):

    aux = 0

    for x in range(1, N+1):

        if (N % x == 0):

            aux += 1

    if (aux == 2):

        return True

    else:

        return False


def entre_primo(X, Y):

    aux = 0

    for x in range(X+1, Y):

        if (primo(x) == True):

            print(x)
            aux = 1

    if (aux == 0):

        print('\nNão existe número primo nesse intervalo')


N1 = int(input('Digite um número: '))

if (primo(N1)):

    print('True')

else:

    print('False')

N2 = int(input('\nDigite o primeiro numero: '))
N3 = int(input('\nDigite o segundo numero: '))

if (N2 < N3):

    entre_primo(N2, N3)

if (N2 == N3):

    print('\nNúmeros iguais portanto não tem primos entre eles')

else:

    N2 = (N2+N3)
    N3 = (N2-N3)
    N2 = (N2-N3)

    entre_primo(N2, N3)
