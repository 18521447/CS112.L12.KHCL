from collections import Counter

def get_all_k(n):
    step = 1 if n % 2 == 0 else 2
    all_k = range(1, n // 2 + 1, step)
    return [k for k in all_k if n % k == 0]

def solve(n, arr) -> str:
    solutions = dict()

    for k in get_all_k(n):
        solutions[k] = [1, 1]

        c = n // k

        first_block = Counter(arr[:k])
        second_block = Counter(arr[k:2*k])

        if first_block == second_block:
            solutions[k] = -1
            continue

        for start in range(2 * k, n, k):
            current_block = Counter(arr[start:start + k])
            if current_block == first_block:
                solutions[k][0] += 1
            elif current_block == second_block:
                solutions[k][1] += 1
            else:
                solutions[k] = -1
                break
    
    count_valid_solution = 0

    result = []
    for key, value in solutions.items():
        if value != -1:
            count_valid_solution += 1

            if value[0] < value[1]:
                value[0], value[1] = value[1], value[0]

            result.append('{} {} {}'.format(key, value[0], value[1]))
            result.append('\n')

    if count_valid_solution == 0:
        return '-1'

    result.pop(-1)
    result.insert(0, '{}\n'.format(count_valid_solution))

    return ''.join(result)
        


if __name__ == '__main__':
    N = int(input().strip())
    A = tuple(map(int, input().split()))

    assert(len(A) == N)

    print(solve(N, A))
