from itertools import combinations


def and_operator(iterable):
    result = ~0
    for elem in iterable:
        result &= elem
    return result


n, k = map(int, input().split())
arr = map(int, input().split())

found = False

for combination in combinations(arr, k):
    if and_operator(combination) == 0:
        found = True
        break

print('YES') if found else print('NO')
