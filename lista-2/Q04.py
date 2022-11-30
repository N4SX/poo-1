def ordenar(s):
    
    lista_original = list(s)
    
    for x in range(len(lista_original)-1, 0, -1):

        for i in range(x):

            if(lista_original[i] > lista_original[i+1]):

                aux = lista_original[i]
                lista_original[i] = lista_original[i+1]
                lista_original[i+1] = aux
    
    palavraOrdenada = ''.join(lista_original)
    
    print('Ordem por letra do alfabeto: {}'.format(palavraOrdenada))

palavra = input('Digite a palavra: ')
(ordenar(palavra))