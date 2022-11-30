
from pessoa import Cliente
from conta import ContaCorrente, ContaPoupanca, SeguroVida
from manipulador_tributavel import Manipulador_tributavel

class Banco():

    def __init__(self):
        self._dicionario_clientes = {}
        self._dicionario_funcionarios = {}
        self._dicionario_conta_c = {}
        self._dicionario_conta_p = {}
        self._dicionario_seguro_vida = {}
        self._lista_historico_tributacoes = []

    def add_cliente(self, nome, cpf, data_nascimento):
        c = Cliente(nome, cpf, data_nascimento)
        if cpf not in self._dicionario_clientes.keys():
            self._dicionario_clientes[cpf] = c
            return True, 'Cliente adicionado com sucesso!'
        else:
            return False, 'Cliente já cadastrado!'


    def add_conta_corrente(self, numero, saldo, cpf):
        if cpf in self._dicionario_clientes.keys():
            cliente = self._dicionario_clientes[cpf]
        else:
            return False, 'Cliente não cadastrado no banco!'
        cc = ContaCorrente(numero, saldo, cliente)
        if cpf not in self._dicionario_conta_c.keys():
            self._dicionario_conta_c[cpf] = cc
            return True, 'Conta adicionada com sucesso!'
        else:
            return False, 'Cliente já tem conta corrente!'

    def add_seguro_vida(self, valor_mensal, valor_total, cpf):
        if cpf in self._dicionario_clientes.keys():
            cliente = self._dicionario_clientes[cpf]
        else:
            return False, 'Cliente não cadastrado no banco!'
        sv = SeguroVida(valor_mensal, valor_total, cliente)

        if cpf not in self._dicionario_seguro_vida.keys():
            self._dicionario_seguro_vida[cpf] = [sv]
            return True, 'Seguro de vida adicionado com sucesso!'
        else:
            self._dicionario_seguro_vida[cpf].append(sv)
            return True, 'Seguro de vida adicionado com sucesso!'

    def imprimir_seguro_vida(self, cpf):
        if cpf in self._dicionario_seguro_vida.keys():
            for sv in self._dicionario_seguro_vida[cpf]:
                sv.imprimir_seguro_vida()
            return True, ''
        else:
            return False, 'Cliente não tem seguro de vida'

    def calcular_tributacoes(self):
        mt = Manipulador_tributavel()
        total = 0

        for cc in self._dicionario_conta_c.values():
            total+=mt.calcula_imposto(cc)

        for lista_sv in self._dicionario_seguro_vida.values():
            for sv in lista_sv:
                total+=mt.calcula_imposto(sv)

        self._lista_historico_tributacoes.append(total)
        return True, 'Tributação = ' + str(total)

    def imprimir_historico_tributacoes(self):
        for list_ in self._lista_historico_tributacoes:
            print(list_)