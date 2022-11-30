import random

def acertos(gab, cartao1, cartao2, cartao3):
    
    a = [0, 0, 0]
    
    for x in range(0, 13):
        
        if(cartao1[x]==gab[x]):
            a[0] += 1
            
        if(cartao2[x]==gab[x]):
            a[1] += 1
        
        if(cartao3[x]==gab[x]):
            a[2] += 1

    return a

gab = []
a2 = []
a3 = []
a1 = []

for x in range(0, 13):
    
    aux = random.randrange(1, 4)
    gab.append(aux)
    
    aux = random.randrange(1, 4)
    a1.append(aux)
    
    aux = random.randrange(1, 4)
    a2.append(aux)
    
    aux = random.randrange(1, 4)
    a3.append(aux)
    
pontos = acertos(gab, a1, a2, a3)

for x in range(0, 3):
    
    if(pontos[x]==13):

        print('Apostador {} é o vencedor'.format(x+1))
        
    else:

        print('Apostador {} obteve {} acertos'.format(x+1,pontos[x]))