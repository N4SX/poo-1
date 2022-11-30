def f_iterativo(num):

    if (num == 0 or num == 1):

        return 1

    else:

        fat = 1
        while (num > 1):

            fat *= num
            num -= 1

        return fat


def f_recursivo(n):

    if (n == 1 or n == 0):

        return 1

    else:

        return (n*f_recursivo(n-1))


num = int(input('\nDigite um número: '))
opcao = int(input(
    '\nDigite o número para o método desejado: \n1-Iterativo \n2-Recursivo \n3-Terminar \n'))

if (opcao == 1):

    metodo = f_iterativo(num)
    print('Calculando {}! = {}'.format(num, metodo))

elif (opcao == 2):

    metodo = f_recursivo(num)
    print('Calculando {}! = {}'.format(num, metodo))

else:

    print('FIM')
