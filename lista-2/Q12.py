dis = {}

def media(dados):

    cond = True
    for chave, lis_temp in dados.items():

        if cond:

            media = sum(lis_temp) / len(lis_temp)
            lista = [chave, media]
            cond = False
        else:

            verifica_media = sum(lis_temp)/len(lis_temp)
            if(verifica_media < media):

                lista.clear()
                media = verifica_media
                lista = [chave, media]
    return lista


def melhor(dados):

    cond = True
    for chave, lis_temp in dados.items():

        if cond:

            minimo = min(lis_temp)

            lista = [chave, minimo, lis_temp.index(minimo)]
            cond = False  
        else:

            if(min(lis_temp) < minimo):

                lista.clear()
                minimo = min(lis_temp)
                lista = [chave, minimo, lis_temp.index(minimo)]
    return lista

for i in range(5):

    nome = input('Nome do corredor: ')

    tempos = [0] * 3
    for i in range(3):

        print('Tempo da volta = {}'.format(i+1))
        tempos[i] = float(input())

    dis.update({nome: tempos})

print(dis)

lista1 = melhor(dis)
print('Corredor: {}, teve o melhor tempo: {}, na volta: {}'.format(lista1[0], lista1[1], lista1[2] + 1))
lista2 = media(dis)
print('O vencedor {} com media {:.2f}'.format(lista2[0], lista2[1]))