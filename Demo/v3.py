k, t = list(map(int, input().split()))

res = t % k

if t % k == 0:
    res = t
else:
    t % k

print(res)
