from his import Historico

class Estoque:
    ''' Classe para representar o estoque de produtos'''
    def __init__(self, nome_produto: str, quantidade: int, codigo: int, limite = 100):
        self._nome_produto = nome_produto
        self._limite = limite
        self._quantidade = quantidade
        self._codigo = codigo
        self._historico = Historico()
 
    def mostra_produto(self):
        
        print('\nNome do produto: {}'.format(self._nome_produto))
        print('Quantidade: {}'.format(self._quantidade))
        print('Codigo: {}'.format(self._codigo))

    def vende(self,valor):
        ''' Mesmo do vendedor la do x1, o vendedor vende chamando essa função'''
        if(self._quantidade - valor < 0):
            return False, '\nQuantidade de requisição exede o estoque !!'
        else:
            self._quantidade -= valor
            self._historico.adicionar('Venda: {} de {}'.format(valor,self._nome_produto))
            return True, '\nVendido com sucesso'

    def repoem(self, valor):
        
        if(self._quantidade + valor > self._limite):
            return False, '\nA quantidade de produtos excede o limite!!'
        else:
            self._quantidade +=valor
            self._historico.adicionar('Reposicao: {} de {}'.format(valor,self._nome_produto))
            return True, '\n Estoque reposto'

    def imprimir_historico(self):
        ''' Mostra o historico, ex: reposição de (10) de coca'''
        if(self._historico):
            self._historico.imprimir()
        else:
            print('\nNao foram feitas operaçoes')