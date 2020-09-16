k, t = list(map(int, input().split()))


current = 0
isIncreasing = True
array = []

for i in range(0, 1000):
    array.append(current)
    if i != 0 and i % k == 0:
        isIncreasing = not isIncreasing
    
    if isIncreasing:
        current += 1
    else:
        current -= 1

print(array[t])
