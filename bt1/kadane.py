n = int(input())

arr = list(map(int, input().split()))

max_global = max_current = arr[0]

max_l = max_r = l = 0

for r in range(1, n):
    tmp = max_current + arr[r]
    if arr[r] > tmp:
        max_current = arr[r]
        l = r
    else:
        max_current = tmp

    if max_current > max_global:
        max_global = max_current
        max_l = l
        max_r = r

print(max_l + 1, max_r + 1, max_global)

