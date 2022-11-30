from Q01 import Pessoa
a = input('Digite o nome: ')
b = int(input('Digite o ano de nascimento: '))
c = float(input('Digite a altura: '))
c = Pessoa(a,b,c)

c.imprimir()
c.cal_idade()