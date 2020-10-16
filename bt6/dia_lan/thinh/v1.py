MAX = 13
def add(arr, bin_num):
    bin_num = bin_num[2:]
    bin_len = len(bin_num)
    for i in range(bin_len):
        arr[i + MAX - bin_len] += int(bin_num[i])

def subtract(arr, bin_num):
    bin_num = bin_num[2:]
    bin_len = len(bin_num)
    for i in range(bin_len):
        arr[i + MAX - bin_len] -= int(bin_num[i])

if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = tuple(map(bin, map(int, input().split())))

    count = [0 for _ in range(MAX)]

    for i in range(k):
        add(count, arr[i])
    
    found = False
    for i in range(1, n - k + 1):
        if k not in count:
            found = True
            break
        subtract(count, arr[i - 1])
        add(count, arr[i + k - 1])
    if k not in count:
        found = True
    
    if found:
        print("YES")
    else:
        print("NO")
