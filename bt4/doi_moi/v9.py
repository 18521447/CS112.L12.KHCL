import math


def advanced_binary_search(n, left, right):
    day = 1


    while left <= right:
        mid = (left + right) // 2
        if total_tree_at(mid) < n:
            left = mid + 1
        else:
            day = mid
            right = mid - 1
    return day


def total_tree_at(x):
    return a * (x - x // k) + b * (x - x // m)


if __name__ == '__main__':
    a, k, b, m, n = map(int, input().split())

    left = right = 1

    while total_tree_at(right) < n:
        left = right
        right *= 2

    day = advanced_binary_search(n, left, right)

    print(day)