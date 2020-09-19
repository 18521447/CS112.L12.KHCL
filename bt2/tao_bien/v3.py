MOD = 10 ** 9 + 7

def next_interleaving_fib(a, b):
    if a == -1:
        return 1, 1
    if a == 1 and b == 1:
        return 1, 2
    return (a + b) % MOD, (a + b + b) % MOD


def main(n, k):
    total = 0
    a, b = -1, 0

    for i in range(k + 1):
        a, b = next_interleaving_fib(a, b)
        total = (total + a) % MOD

    return n * total % MOD

if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    print(main(n, k))
