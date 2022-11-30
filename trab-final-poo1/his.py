''' Classe para armazenar as transações '''
class Historico:

    def __init__(self):
        self._transacoes = [] 
        ''' Lista para armazenar as transações '''

    def adicionar(self, mensagem: str):
        self._transacoes.append(mensagem)
        ''' Função para adicionar na lista as operação'''

    def imprimir(self):
        ''' Saida de dados para mostrar o historico '''
        for t in self._transacoes:
            print(t)
