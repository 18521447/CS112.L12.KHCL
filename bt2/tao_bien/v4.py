 
MOD = 1000000007

def custom_fib(n):
    if n == 0 or n == 1:
        return [1, 1]
    
    a, b = custom_fib(n // 2)

    c = (a ** 2 + b ** 2) % MOD
    d = (2 * a * b - b ** 2) % MOD
    e = (c + d) % MOD

    if n % 2 == 0:
        return [c, d]
    else:
        return [e, c]

n, k = map(int, input().split())

result = (custom_fib(2 * k)[0] * n) % MOD

print(result)
