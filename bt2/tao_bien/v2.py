ratios = [ 2,
           2.5,
           2.6,
           2.6153846153846154,
           2.6176470588235294,
           2.6179775280898876,
           2.6180257510729614,
           2.6180327868852458,
           2.618033813400125,
           2.6180339631667064,
           2.618033985017358,
           2.618033988205325,
           2.6180339886704433,
           2.618033988738303,
           2.618033988748204,
           2.618033988749648,
           2.618033988749859,
           2.6180339887498896,
           2.618033988749894,
           2.618033988749895]

MOD = 10 ** 9 + 7

def main(n, k):
    result = n

    i = 0
    while i < len(ratios):
        result *= ratios[i]
        if i + 1 == k:
            break
        i += 1
    
    if i == len(ratios):
        ratio = 1
        while i < k:
            ratio *= ratios[-1]
            ratio = ratio % MOD
            i += 1
        result = int((result * ratio) % MOD)
    
    return int(result)

if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    print(main(n, k))
