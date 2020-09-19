MOD = 10 ** 9 + 7

def fib(n):
    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n + 1)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':    v1, v2, v3 = v1+v2, v1, v2
    return v2


def interleaving_fib(n):
    return fib(n * 2 - 1)


def main(n, k):
    total = 0
    for i in range(k + 1):
        total = (total + interleaving_fib(i)) % MOD
        
    return n * total % MOD

if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    print(main(n, k))
