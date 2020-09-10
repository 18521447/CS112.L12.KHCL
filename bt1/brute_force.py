input()

arr = list(map(int, input().split()))

max_global = arr[0]
max_l = 1
max_r = 1

for i in range(len(arr)):
    for j in range(i, len(arr)):
        
        max_current = sum(arr[i:j + 1])

        if max_global < max_current:
            max_global = max_current
            max_l = i + 1
            max_r = j + 1

        
print('{} {} {}'.format(max_l, max_r, max_global))
