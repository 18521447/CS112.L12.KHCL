def find(vertex_info, i):
    if vertex_info[0][i] == i:
        return i
    else:
        parent = find(vertex_info, vertex_info[0][i])
        vertex_info[0][i] = parent
        return parent


def union(vertex_info, v1, v2):
    parent1 = find(vertex_info, v1)
    parent2 = find(vertex_info, v2)

    if parent1 == parent2:
        return False
    else:
        vertex_info[0][parent1] = parent2
        vertex_info[1][parent2] += vertex_info[1][parent1]

    return True


def is_root(vertex_info, v):
    return vertex_info[0][v] == v


def solve():
    MOD = 1_000_000_007
    n, m = map(int, input().split())

    # vertex_info[0] saves parents
    # vertex_info[1] saves number of connected components at the root vertex
    vertex_info = []
    vertex_info.append([_ for _ in range(n)])
    vertex_info.append([1 for _ in range(n)])

    for _ in range(m):
        v1, v2 = map(int, input().split())
        union(vertex_info, v1 - 1, v2 - 1)

    root_indices = []
    total_possible_ways = 1

    for i in range(n):
        if is_root(vertex_info, i):
            root_indices.append(i)
            total_possible_ways = (
                total_possible_ways * vertex_info[1][i]) % MOD

    total_new_pipe = len(root_indices) - 1

    return total_new_pipe, total_possible_ways


if __name__ == '__main__':
    answers = solve()
    print(answers[0])
    print(answers[1])
