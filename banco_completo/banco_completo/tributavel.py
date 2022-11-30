import abc

class Tributavel(abc.ABC):

    @abc.abstractmethod
    def get_valor_tributado(self):
        ''' Esse metodo devera retornar o valor a ser tributado da classe'''
        pass