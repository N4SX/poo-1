from x1 import Gerente
from x1 import Vendedor

''' Operações auxiliares para iniciar os produtos'''
p = Gerente('Diego',123,5000)
p.adiciona_produto('HD',50,1)
p.adiciona_produto('RAM',100,2)
p.adiciona_produto('PLACA MAE',10,3)
p.adiciona_produto('GABINETE',10,4)
f = Vendedor('Marcelo',123456,2000)

def menu_principal():
    ''' Menu inicial para iniciar as operações'''
    while(True):
        try:
            print('\n(1) - Entrar como Gerente')
            print('(2) - Entrar como Funcionario')
            op = int(input('Opção: '))

            if op == 1:
                menu_gerente(p)
            elif op == 2:
                menu_vendedor(f)
        except ValueError:
            print('\nOpção invalida, progama finalizado')
            break


def menu_gerente(p):
    ''' Menu secundario com as operações para o gerente'''
    while(True):
        try:
            print('\n(1) - Mostrar Lista de produtos')
            print('(2) - Adicionar Produto')
            print('(3) - Remover produto')
            op = int(input('Opção: '))

            if op == 1:
                p.mostra_lista()
            elif op == 2:
                nome = input('Nome do produto: ')
                quant = int(input('Quantidade: '))
                codi = int(input('Codigo do produto: '))
                p.adiciona_produto(nome,quant,codi)
            elif op == 3:
                codi = int(input('Codigo do produto a ser Removido: '))
                p.remove_produto(codi)
        except ValueError:
            print('\nOpção invalida, menu do gerente finalizado')
            break

        
def menu_vendedor(f):
    ''' Menu secundario com as operações do vendedor'''
    while(True):
        try:
            print('\n(1) Mostra Lista de produtos')
            print('(2) - Vender produto')
            print('(3) - Repor produto')
            print('(4) - Historico de venda')
            op = int(input('Opção: '))

            if op == 1:
                f.mostra_lista()

            elif op == 2:
                a = int(input('Informe o codigo do produto: '))
                b = int(input('Qunatidade de itens a serem vendidos: '))
                f.vender(a,b)
            
            elif op == 3:
                a = int(input('Informe o codigo do produto: '))
                b = int(input('Qunatidade de itens a serem reabastecidos: '))
                f.repor(a,b)

            elif op == 4:
                f.imprimir()
        except ValueError:
            print('\nOpção invalida, menu do gerente finalizado')
            break

''' inicia o menu inicial'''
menu_principal()