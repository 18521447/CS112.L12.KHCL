from sys import stdin, stdout
from collections import Counter

no = 'NO\n'
yes = 'YES\n'


def solve() -> str:
    start1, end1, start2, end2 = map(lambda x: int(x) - 1, stdin.readline().split())

    if end1 - start1 != end2 - start2:
        return no
    elif start1 == start2:
        return yes

    if start2 < start1:
        start1, start2 = start2, start1
        end1, end2 = end2, end1

    if start2 <= end1:
        overlap = end1 - start2 + 1
        end1 -= overlap
        start2 += overlap

    s1 = s[start1: end1 + 1]
    s2 = s[start2: end2 + 1]
    if Counter(s1) == Counter(s2):
        return yes
    return no


if __name__ == '__main__':
    s = stdin.readline().strip()
    q = int(stdin.readline().strip())

    for _ in range(q):
        stdout.writelines(solve())
