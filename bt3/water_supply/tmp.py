import sys

def bfs(u, a, tplt, cha, num_tplt):
    q = [u]
    while len(q) > 0:
        u = q.pop(0)
        tplt[num_tplt] += 1
        for v in a[u]:
            if cha[v] == 0:
                cha[v] = 1
                q.append(v)

t = sys.stdin.readline().split()
n,m = [int(x) for x in t[:2]]
a = [[] for _ in range(n)]
cha = [0 for _ in range(n)]
tplt = [0 for _ in range(n)]

for i in range(m):
    t = sys.stdin.readline().split()
    u,v = [int(x) for x in t]
    if u < 1 or v < 1: continue
    if u > n or v > n: continue
    a[u-1].append(v-1)
    a[v-1].append(u-1) 

num_tplt = 0
for u in range(n):
    if cha[u] == 0:
        cha[u] = 1
        # dfs(u, a, tplt, cha, num_tplt)
        bfs(u, a, tplt, cha, num_tplt)
        num_tplt += 1
print(num_tplt - 1)
    
def mul(x, y):
    if y == 0: return 1
    t = mul(x, y//2)
    t = (t * t)
    if y % 2 == 0: 
        return t
    return (t * x)
        

if (num_tplt == 1):
    print(0)
else:
    res = 1
    for x in tplt[:num_tplt]:
    #  print(tplt[i])
        res = res * x
    print(res)
    res = (res * mul(n, num_tplt-2)) % (1000000007)
    print(res) 