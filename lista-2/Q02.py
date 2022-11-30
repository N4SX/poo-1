def imprimir(s):
    
    for x in s:

        if(list==type(x)):

            imprimir(x)
            
        else:

            print(x)

lista = [0,1,[2,[3,4]],5]
imprimir(lista)