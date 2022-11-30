lista = []
a = []
i = 0

while(i != 10):

    item = input('Digite um item na lista: ')
    lista.append(item)
    a.append(item)
    i += 1

lista[0] = a[9]
lista[9] = a[0]
lista[1] = a[8]
lista[8] = a[1]
lista[2] = a[7]
lista[7] = a[2]
lista[3] = a[6]
lista[6] = a[3]
lista[4] = a[5]
lista[5] = a[4]

print(lista)