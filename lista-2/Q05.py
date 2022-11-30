import random

num_randon = random.randrange(0, 100)

aux = 1

while(aux<=10):

    num = int(input('Descubra o número, tentativa {}:'.format(aux)))
    aux += 1

    if(num==num_randon):
        
        print('ACERTOU!')
        opcao = input('Continue?s/n\n')
        
        if(opcao=='s'):

            num_randon = random.randrange(0, 100)
            aux = 1
        else:

            break

print("Voce perdeu o número secreto era = {}".format(num_randon))