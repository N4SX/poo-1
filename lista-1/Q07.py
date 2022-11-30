def binario(a):

    if (a == 0):

        print(0)

    while (a >= 1):

        n = 0
        x = int(a % 2)
        print(x)
        a /= 2
        n += 1


a = int(input('Digite um numero: '))
binario(a)
