from pessoa import Cliente
from conta import ContaCorrente, ContaPoupanca, SeguroVida
from tributavel import Tributavel
from banco import Banco


def menu():
    print('1 - Add cliente\n2 - Add conta corrente\n3 - Add seguro de vida\n4 - Imprimir seguro de vida\n 5 - Calcular tributação\n')
    return int(input('Digite a opção desejada: '))

def pegar_cliente():
    nome = input('Digite o nome do cliente: ')
    cpf = input('Digite o cpf do cliente: ')
    data_nascimento = input('Digite a data de nascimento do cliente: ')
    return b.add_cliente(nome, cpf, data_nascimento)

def pegar_conta_corrente():
    numero = input('Digite o numero da conta: ')
    saldo = float(input('Digite o saldo da conta: '))
    cpf = input('Digite o cpf do cliente: ')
    return b.add_conta_corrente(numero, saldo, cpf)

def pegar_seguro_vida():
    valor_mensal = float(input('Digite o valor mensal: '))
    valor_total = float(input('Digite o valor total: '))
    cpf = input('Digite o cpf do cliente: ')
    return b.add_seguro_vida(valor_mensal, valor_total, cpf)

def imprimir_seguro_vida():
    cpf = input('Digite o cpf do cliente: ')
    return b.imprimir_seguro_vida(cpf)

b = Banco()
Tributavel.register(ContaCorrente)
Tributavel.register(SeguroVida)
while True:

    op = menu()

    if op == 1:
        retorno, mensagem = pegar_cliente()
        print(mensagem)

    elif op == 2:
        retorno, mensagem = pegar_conta_corrente()
        print(mensagem)

    elif op == 3:
        retorno, mensagem = pegar_seguro_vida()
        print(mensagem)

    elif op == 4:
        retorno, mensagem = imprimir_seguro_vida()
        print(mensagem)

    elif op == 5:
        retorno, messagem = b.calcular_tributacoes()
        print(messagem)

    elif op == 6:
        b.imprimir_historico_tributacoes()