import random

lista1 = []
lis_ord = []

for x in range(0, 100):
    
    num = random.randrange(1, 101)
    
    lista1.append(num)

s = sum(lista1)
media = s/100

lis_ord = lista1.copy()
lis_ord.sort()

s_mediana = lis_ord[50] + lis_ord[51]
mediana = s_mediana/2

print("Media {}\nMediana {}".format(media, mediana))