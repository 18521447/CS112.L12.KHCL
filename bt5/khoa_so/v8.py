from collections import Counter

def solve(lock: str) -> str:
    counter = Counter(lock)
    keys = sorted(counter.keys(), reverse=True)
    final_mod = int(lock) % 3

    if final_mod != 0:
        mod1 = None
        mod2 = [None, None]
        i_m2 = 0
        for key in reversed(keys):
            for _ in range(counter[key]):
                current_mod = int(key) % 3
                if current_mod == final_mod:
                    mod1 = key
                    break
                elif current_mod != 0 and i_m2 < 2:
                    mod2[i_m2] = key
                    i_m2 += 1
            if mod1:
                break
        
        if mod1:
            counter[mod1] -= 1
        else:
            counter[mod2[0]] -= 1
            counter[mod2[1]] -= 1
            
    unlock = []
    for key in keys:
        for _ in range(counter[key]):
            unlock.append(key)
    return ''.join(unlock)


if __name__ == '__main__':
    lock = input().strip()
    unlock = solve(lock)
    print(unlock)