from collections import Counter

def solve(string):
    a, b, c, d = map(int, input().split())
    e = max(b - c, 0)
    if e > 0:
        s1 = Counter(string[a-1:b-e-1])
        stmp = Counter(string[b-e:b])
        s2 = Counter(string[c+e:d])
        s1 += stmp
        s2 += stmp
    else:
        s1 = Counter(string[a-1:b])
        s2 = Counter(string[c-1:d])
    if s1 == s2:
        print('YES')
        return
    print('NO')

s = input().strip()
q = int(input())

for _ in range(q):
    solve(s)

# e=2
# 1 5 3 7
# 1 2 3 4 5 6 7
# 0 1 2 3 4 5 6
# 1 2
# 3 5
# 6 7
