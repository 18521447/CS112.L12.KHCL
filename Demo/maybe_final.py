k, t = list(map(int, input().split()))

double = k * 2
result = t % double

if result > k:
    result = k - result % k

print(result)
