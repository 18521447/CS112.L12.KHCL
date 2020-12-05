from typing import List


class KSum:
    def __init__(self, idx, sum, k, n):
        self.value: int = sum

        self.index: int = idx

        left_bound = max(self.index - k + 1, 0)
        right_bound = min(self.index + k, n - k + 1)

        self.affected_range = range(left_bound, right_bound)

    def __repr__(self):
        start = self.affected_range.start
        stop = self.affected_range.stop
        return '{} {} {} {}'.format(self.value, self.index, start, stop)


if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    sum_first_k_num = sum(a[:k])
    prev_sum = KSum(0, sum_first_k_num, k, n)
    max_sum = prev_sum
    all_sums: List[KSum] = [prev_sum]

    for i in range(1, n - k + 1):
        current_sum_value = prev_sum.value - a[i - 1] + a[i + k - 1]
        current_sum = KSum(i, current_sum_value, k, n)
        all_sums.append(current_sum)
        if current_sum.value > max_sum.value:
            max_sum = current_sum
        prev_sum = current_sum

    prev_left_max = all_sums[0].value - 1
    max_so_far_from_left = []
    prev_right_max = all_sums[-1].value - 1
    max_so_far_from_right = []
    
    for left_index in range(len(all_sums)):
        right_index = len(all_sums) - 1 - left_index

        left_max = max(prev_left_max, all_sums[left_index].value)
        max_so_far_from_left.append(left_max)
        prev_left_max = left_max

        right_max = max(prev_right_max, all_sums[right_index].value)
        max_so_far_from_right.insert(0, right_max)
        prev_right_max = right_max

    min_sum = max_sum
    for i in max_sum.affected_range:
        tmp_min_sum = all_sums[i]
        left_bound = tmp_min_sum.affected_range.start - 1
        right_bound = tmp_min_sum.affected_range.stop
        tmp_min_is_valid = True
        if left_bound >= 0:
            if max_so_far_from_left[left_bound] > tmp_min_sum.value:
                tmp_min_is_valid = False
        if right_bound < len(all_sums):
            if max_so_far_from_right[right_bound] > tmp_min_sum.value:
                tmp_min_is_valid = False
        if tmp_min_sum.value >= min_sum.value:
            tmp_min_is_valid = False
        if tmp_min_is_valid:
            min_sum = tmp_min_sum

    
    print(min_sum.value)

    