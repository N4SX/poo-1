import abc
from datetime import datetime

class HistoricoTransacao():

    def __init__(self):
        self._data_abertura = datetime.today()
        self._transacoes = []

    def add_transacao(self, str):
        self._transacoes.append(str)

    def imprimir_transacoes(self):
        print('Conta aberta em: ', self._data_abertura)
        for t in self._transacoes:
            print(t)

class Conta(abc.ABC):

    def __init__(self, numero, saldo, cliente):
        self._numero = numero
        self._saldo = saldo
        self._cliente = cliente
        self._historico = HistoricoTransacao()

    def sacar(self, valor):
        self._saldo -= valor
        self._historico('Saque realizado, valor: ' + str(valor) + str(datetime.now()))
        return True

    def depositar(self, valor):
        self._saldo += valor
        self._historico('Deposito realizado, valor: ' + str(valor) + str(datetime.now()))
        return True

    def transferir(self, destino, valor):
        self._saldo -= valor
        destino.depositar(valor)
        self._historico('Transferencia realizada valor: ' + str(valor) + str(datetime.now()))
        return True

    def imprimir_transacoes(self):
        self._historico.imprimir_transacoes()


class ContaCorrente(Conta):

    def __init__(self, numero, saldo, cliente, limite=0):
        super().__init__(numero, saldo, cliente)
        self._limite = limite

    def get_valor_tributado(self):
        return (self._saldo*1/100) + 10


class ContaPoupanca(Conta):

    def __init__(self, numero, saldo, cliente):
        super().__init__(numero, saldo, cliente)


class SeguroVida():

    def __init__(self, valor_mensal, valor_total, cliente):
        self._valor_mensal = valor_mensal
        self._valor_total = valor_total
        self._cliente = cliente

    def imprimir_seguro_vida(self):
        print(self._valor_mensal, self._valor_total)
        self._cliente.imprimir_cliente()

    def get_valor_tributado(self):
        return self._valor_mensal*2/100
