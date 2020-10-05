from random import randint

arr = [i**2 for i in range(1, 201)]

test = [randint(1, 40000) for i in range(1000000)]


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

    if get_value_at(mid) < n:
        return mid + 1
    else:
        return mid - 1


def get_arr(i):
    return arr[i]

def normal_search(get_value_at, n, left, right):
    for i in range(left, right + 1):
        if get_value_at(i) >= n:
            return i

if __name__ == '__main__':
    r = []
    for t in test:
        r.append(normal_search(get_arr, t, 0, len(arr) - 1) ==
                 advanced_binary_search(get_arr, t, 0, len(arr) - 1))

    print(all(r))