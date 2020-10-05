import math


def advanced_binary_search(get_value_at, n, left, right):
    mid = (left + right) // 2
    while left <= right:
        if get_value_at(mid) == n:
            return mid
        if get_value_at(mid) < n:
            left = mid + 1
        else:
            right = mid - 1
        mid = (left + right) // 2

    right += 50
    left = 0 if left < 50 else left - 50
    for mid in range(left, right + 1):
        if get_value_at(mid) >= n:
            return mid


def total_tree_at(x):
    return a * (x - x // k) + b * (x - x // m)


if __name__ == '__main__':
    a, k, b, m, n = map(int, input().split())

    left_day = right_day = 1
    
    while total_tree_at(right_day) < n:
        left_day = right_day
        right_day *= 2
        
    for day in range(left_day, right_day + 1):
        if total_tree_at(day) >= n:
            break

    print(day)
