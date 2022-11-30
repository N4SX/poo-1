from x2 import Estoque
from ex_abstrata import Modifica_estoque
import abc

produto = {} 
'''variavel global para referir-se a classe estoque em forma de discionario'''

class Funcionario(abc.ABC):
    ''' Classe prinipal para Funcionario '''
    def __init__(self, nome: str, cpf: int, salario: float):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    ''' Metodos privados '''
    @property
    def nome(self) -> str:
        return self._nome

    @property
    def cpf(self) -> int:
        return self.cpf

    @property
    def salario(self) -> float:
        return self._salario
    
    def info(self):
        ''' Função para mostrar as informações do Funcionario'''
        
        print('\nNome: {}'.format(self._nome))
        print('CPF: {}'.format(self._cpf))
        print('Salario: {}'.format(self._salario))

class Gerente(Funcionario, Modifica_estoque):
    
    def __init__(self, nome, cpf, salario, senha = '0000'):
        self._senha = senha
        super().__init__(nome, cpf, salario)

    def inf(self):
        super().info()
    
    def adiciona_produto(self,nome, quantidade, codigo):

        try:
            p = Estoque(nome,quantidade,codigo)
            produto[codigo] = p
        except:
            print('\n\nFalha em adicionar produto!!\n\n')

    def remove_produto(self, codigo):
        
        try:
            del produto[codigo]
        except:
            print('produto nao existe no estoque')

 
    def mostra_lista(self):
    
        if(produto):
            print('\nLista de Produtos: ')
            for k, v in produto.items(): 
                v.mostra_produto()
        else:
            print('Nao ha produtos cadastrados no estoque')
        

class Vendedor(Funcionario):

    def __init__(self, nome, cpf, salario):
        super().__init__(nome, cpf, salario)

    def mostra_lista(self):
        
        if(produto):
            print('\nLista de Produtos: ')
            for k, v in produto.items():
                v.mostra_produto()
        else:
            print('Nao ha produtos cadastrados no estoque')

    def vender(self,codigo, valor):
        
        if(valor > 0):
            a = produto[codigo].vende(valor)
            if a:
                print(a[1])
        else:
            print('\nValor nao pode ser nulo ou negativo')

    def repor(self, codigo, valor):
        
        a = produto[codigo].repoem(valor)
        if a:
            print(a[1])

    def imprimir(self):
        
        print("\nHistorico de acoes do vendedor:")
        for k, v in produto.items():
            v.imprimir_historico()
        print('\n')