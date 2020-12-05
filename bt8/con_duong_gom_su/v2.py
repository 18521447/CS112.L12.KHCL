from collections import Counter

def get_all_k(n):
    step = 1 if n % 2 == 0 else 2
    all_k = range(1, n // 2 + 1, step)
    return [k for k in all_k if n % k == 0]

def solve(n, arr) -> str:
    solutions = dict()

    for k in get_all_k(n):
        solutions[k] = [0, 0]

        group1 = None
        group2 = None

        for start in range(0, n, k):
            current_block = Counter(arr[start:start + k])
            if current_block == group1:
                solutions[k][0] += 1
            elif current_block == group2:
                solutions[k][1] += 1
            elif group1 is None:
                group1 = current_block
                solutions[k][0] += 1
            elif group2 is None and current_block != group1:
                group2 = current_block
                solutions[k][1] += 1
            else:
                solutions[k] = -1
                break
        
        if isinstance(solutions[k], list) and 0 in solutions[k]:
            solutions[k] = -1
    
    count_valid_solution = 0

    result = []
    for key, value in solutions.items():
        if value != -1:
            count_valid_solution += 1

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

    print(solve(N, A))