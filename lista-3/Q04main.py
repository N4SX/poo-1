from Q04 import ControleRemoto
from Q04 import Televisao

c = ControleRemoto(0, 0)

op = 1
while(op != 0):
    print('1 - Aumentar volume')
    print('2 - Diminuir volume')
    print('3 - Aumentar canal')
    print('4 - Diminuir canal')
    print('5 - Digitar canal')
    print('0 - sair')
    op = int(input('Opcao: '))
    if(op == 0):
        break
    if(op == 1):
        c.aumentaVol()
        input('Digite algo para continuar')
    elif(op == 2):
        c.diminuiVol()
        input('Digite algo para continuar')
    elif(op == 3):
        c.aumentaCal()
        input('Digite algo para continuar')
    elif(op == 4):
        c.diminuiCal()
        input('Digite algo para continuar')
    elif(op == 5):
        c.trocaCanal()
        input('Digite algo para continuar')