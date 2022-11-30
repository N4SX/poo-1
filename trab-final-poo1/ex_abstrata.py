import abc

class Modifica_estoque(abc.ABC):
    ''' Classe abistrata para classes que modificam o estoque diretamente'''

    @abc.abstractmethod
    def adiciona_produto(self,nome, quantidade, codigo):
        '''Metodo para adicionar produtos no estoque'''
        pass

    @abc.abstractmethod
    def remove_produto(self, codigo):
        '''Metodo para remover produtos no estoque'''
        pass