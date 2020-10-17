if __name__ == '__main__':
    gene1 = input().strip()
    gene2 = input().strip()

    gene2_set = set()

    for i in range(len(gene2) - 1):
        doublet = gene2[i:i + 2]
        gene2_set.add(doublet)

    total = 0

    for i in range(len(gene1) - 1):
        doublet = gene1[i:i + 2]
        if doublet in gene2_set:
            total += 1

    print(total)