MOD = 10 ** 9 + 7

def main(n, k):    
    table = []

    table.append([n])

    for i in range(1, k + 1):
        row = table[-1][:]

        total = 0
        for i in range(1, len(row) + 1):
            total += row[i - 1] * i

        row.insert(0, total)
        table.append(row)

    result = sum(table[k]) % MOD
    return result

if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    print(main(n, k))
