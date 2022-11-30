pre = 5.00
qnt = 120
n = 0
c = 0

while (pre > 1):

    d = c
    c = ((pre*qnt)-200)

    if (c > d):

        p_ingresso = pre
        q_total = qnt
        v_max = c

    print('Preço do ingresso = {}, Quantidade = {}, Lucro = {}'.format(pre, qnt, c))

    pre -= 0.5
    qnt += 26
    n += 1

print('\n Valor máximo = {:.2f}\n Preço do ingresso = {:.2f}\n Quantidade vendida = {:.2f}'.format(
    v_max, p_ingresso, q_total))
