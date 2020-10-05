import math

a, k, b, m, n = map(int, input().split())


def total_tree_at(x):
    return a * (x - x // k) + b * (x - x // m)


left_day = right_day = 1

while total_tree_at(right_day) < n:
    left_day = right_day
    right_day *= 2

day = (left_day + right_day) // 2
while left_day <= right_day:
    total_tree_at_day = total_tree_at(day)
    if total_tree_at_day < n:
        left_day = day + 1
    elif total_tree_at_day > n:
        right_day = day - 1
    else:
        break
    day = (left_day + right_day) // 2

print(day)
