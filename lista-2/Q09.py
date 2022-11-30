dados = []
a = []

for x in range(0, 10):
    
    nome = input('Digite o nome: ')
    cep = int(input('Digite o CEP: '))
    end = input('Digite o endereço: ')
    bairro = input('Digite o bairro: ')
    telefone = int(input('Digite o telefone: '))
    
    a.append(end)
    a.append(nome)
    a.append(telefone)
    a.append(bairro)
    a.append(cep)

    dados.append(a)
    a = []

for x in dados:

    print(list(x))