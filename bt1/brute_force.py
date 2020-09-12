n = int(input())

arr = list(map(int, input().split()))

max_global = arr[0]
max_l = 0
max_r = 0

for i in range(n):
    for j in range(i, n):
        
        max_current = sum(arr[i:j + 1])

        if max_global < max_current:
            max_global = max_current
            max_l = i
            max_r = j

        
print('{} {} {}'.format(max_l + 1, max_r + 1, max_global))
