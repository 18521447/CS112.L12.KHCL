import math

a, k, b, m, n = map(int, input().split())

def total_tree_at(x):
    return a * (x - x // k) + b * (x - x // m)

day = 1    

while total_tree_at(day) < n:
    day += 1

print(day)
