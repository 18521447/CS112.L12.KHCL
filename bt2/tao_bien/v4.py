MOD = 10 ** 9 + 7

def main_fib(n):
	if n == 0 or n == -1:
		return (0, 1)
	else:
		a, b = main_fib(n // 2)
		c = a * (b * 2 - a)
		d = a * a + b * b
		if n % 2 == 0:
			return (c, d)
		else:
			return (d, c + d)

def fib(n):
	return main_fib(n)[1]

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
