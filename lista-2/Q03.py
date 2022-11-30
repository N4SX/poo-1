def buscar(s):
    
    letra = input('Buscar qual letra ?: ')
    lista = list(s)
    a = 0
    
    for x in lista:
        
        if(letra==x):

            break
        
        a += 1
  
    return a

p = input('Digite a palavra: ')
pos = buscar(p)
print('Posição = {}'.format(pos))