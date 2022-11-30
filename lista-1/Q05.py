def f_iterativo(num):

    if (num == 0 or num == 1):

        return 1

    else:

        fat = 1
        while (num > 1):

            fat *= num
            num -= 1
        return fat


def f_arranjo(n, p):

    X = f_iterativo(n)
    Y = f_iterativo(n-p)
    va = (X/Y)
    return va


def f_comb(n, r):

    X = f_iterativo(n)
    Y = f_iterativo(r)
    Z = f_iterativo(n-r)
    vcomb = (X/(Y*Z))
    return vcomb


n = int(input('\nQuantidade de números: '))
p = int(input('\nCondição de menor ou igual aos números: '))

a = f_arranjo(n, p)
c = f_comb(n, p)

print('\nO valor do arranjo é = {:.2f}'.format(a))
print('\nO valor da combinação é = {:.2f}'.format(c))
