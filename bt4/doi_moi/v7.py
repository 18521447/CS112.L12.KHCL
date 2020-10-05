import math


def advanced_binary_search(get_value_at, n, left, right):
    day = right
    while left <= right:
        mid = (left + right) // 2
        if get_value_at(mid) == n:
            return mid
        if get_value_at(mid) < n:
            left = mid + 1
        else:
            day = mid
            right = mid - 1
    return day


def total_tree_at(x):
    return a * (x - x // k) + b * (x - x // m)


if __name__ == '__main__':
    a, k, b, m, n = map(int, input().split())

    left_day = 1
    right_day = 1

    while total_tree_at(right_day) < n:
        left_day = right_day
        right_day *= 2

    day = advanced_binary_search(total_tree_at, n, 1, 10**18)

    print(day)
