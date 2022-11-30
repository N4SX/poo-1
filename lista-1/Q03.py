fg = 0
pi = 3.14

while (fg != 4):

    fg = int(input('\nDigite o número da forma geométrica desejada: \n 1-Triângulo\n 2-Quadrado\n 3-Circulo\n 4-Terminar\n'))

    if (fg == 1):

        bt = float(input('Digite a base do triângulo: '))
        alt = float(input('Digite a altura do triângulo: '))
        at = ((bt*alt)/2)
        print('A área do triângulo é = {}'.format(at))

    elif (fg == 2):

        altQ = float(input('Digite a altura do quadrado: '))
        bq = float(input('Digite o base do quadrado: '))
        aq = (bq*altQ)
        print('A área do quadrado é = {}'.format(aq))

    elif (fg == 3):

        ra = float(input('Digite o raio do circulo: '))
        ac = (pi*ra**2)
        print('A área da circunferência é = {:.2f}'.format(ac))

    else:

        print('FIM')
