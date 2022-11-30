import abc

class Pessoa(abc.ABC):

    def __init__(self, nome, cpf, data_nascimento):
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento

    def imprmir_pessoa(self):
        print(self._nome, self._cpf)


class Funcionario(Pessoa):

    def __init__(self, nome, cpf, data_nascimento, salario):
        super().__init__(nome, cpf, data_nascimento)
        self._salario = salario

    def imprimir_funcionario(self):
        super().imprmir_pessoa()
        print(self._salario)


class Cliente(Pessoa):

    def __init__(self, nome, cpf, data_nascimento, profissao = 'desempregado', renda=0):
        super().__init__(nome, cpf, data_nascimento)
        self._profissao = profissao
        self._renda = renda

    def imprimir_cliente(self):
        super().imprmir_pessoa()
        print(self._profissao, self._renda)