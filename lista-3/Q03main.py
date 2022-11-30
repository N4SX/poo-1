from Q03 import Elevador

c = Elevador(0,0,0,0)

total = int(input('Digite o total de andares: '))
cap = int(input('Digite a capacidade maxima de pessoas: '))
c.inicializa(total, cap)

while(1):
    print('Opcoes: ')
    print('1 - Entra')
    print('2 - Sai')
    print('3 - Sobe')
    print('4 - Desce')
    print('0 - Parar')
    op = input('Opcao: ')
    if(op == '0'):
        break
    elif(op == '1'):
        c.entra()
    elif(op == '2'):
        c.sai()
    elif(op == '3'):
        c.sobe()
    elif(op == '4'):
        c.desce()