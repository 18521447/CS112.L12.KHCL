from random import randint

def total_tree_at(x, a, k, b, m):
    return a * (x - x // k) + b * (x - x // m)

for T in range(5, 1006):
    inp = open('inp/' + str(T), mode='w')
    out = open('out/' + str(T), mode='w')

    a = randint(1, 520)
    b = randint(1, 723)
    k = randint(2, 3012340)
    m = randint(2, 1023450)
    n = randint(1, 2000134)

    day = 1    

    while total_tree_at(day, a, k, b, m) < n:
        day += 1
    
    inp.write('{} {} {} {} {}'.format(a, k, b, m, n))
    out.write('{}\n'.format(day))
