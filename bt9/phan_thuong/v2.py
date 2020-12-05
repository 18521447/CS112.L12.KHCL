def k_sums_len(n, k):
    return n - k + 1


def left_bound(idx, k):
    return idx - k


def right_bound(idx, k):
    return idx + k


def inbound(idx, other, k):
    return left_bound(other, k) < idx and idx < right_bound(other, k)


def range_start_index(idx, k, n):
    return max(0, left_bound(idx, k) + 1)


def range_stop_index(idx, k, n):
    return min(k_sums_len(n, k), right_bound(idx, k))


def max_so_far(arr):
    n = len(arr)

    from_left = [0] * n
    from_right = [0] * n
    max_so_far_from_left = arr[0]
    max_so_far_from_right = arr[-1]

    for i, j in zip(range(n), reversed(range(n))):
        max_so_far_from_left = max(arr[i], max_so_far_from_left)
        max_so_far_from_right = max(arr[j], max_so_far_from_right)
        from_left[i] = max_so_far_from_left
        from_right[j] = max_so_far_from_right

    return from_left, from_right


def calculate_k_sums_and_max(arr, k):
    n = len(arr)
    current_sum = sum(arr[:k])
    current_max = current_sum
    sums = [current_sum]

    for i in range(1, k_sums_len(n, k)):
        current_sum = current_sum - arr[i - 1] + arr[i + k - 1]
        current_max = max(current_max, current_sum)
        sums.append(current_sum)

    return sums, current_max


def solve(a, k, n):
    sums, max_sum = calculate_k_sums_and_max(a, k)

    max_indices = []

    for i in range(len(sums)):
        if sums[i] == max_sum:
            max_indices.append(i)

    first_max_index = max_indices[0]
    last_max_index = max_indices[-1]

    intersection_start = range_start_index(last_max_index, k, n)
    intersection_stop = range_stop_index(first_max_index, k, n)

    if not inbound(intersection_start, first_max_index, k):
        return max_sum

    max_from_left, max_from_right = max_so_far(sums)

    min_sum = max_sum

    for i in range(k_sums_len(n, k)):
        tmp_min = sums[i]

        if tmp_min >= min_sum:
            continue

        l_bound = left_bound(i, k)
        r_bound = right_bound(i, k)

        if l_bound >= 0:
            if tmp_min < max_from_left[l_bound]:
                continue

        if r_bound < k_sums_len(n, k):
            if tmp_min < max_from_right[r_bound]:
                continue

        min_sum = tmp_min

    return min_sum


if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    print(solve(a, k, n))
