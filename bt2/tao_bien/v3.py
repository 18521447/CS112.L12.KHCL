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


# 0 1 2 3 4 5 6  7  8  9  10 11  12  13
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377

# 1 1   3   8    21    55    144     377
# 0 1   2   3    4     5     6       7

