from collections import Counter

def counter_to_str(sorted_keys, counter) -> str:
    string = []

    for key in sorted_keys:
        string.append(key * counter[key])
    
    return ''.join(string)

def solve(lock: str) -> str:
    counter = Counter(lock)
    keys = sorted(counter.keys(), reverse=True)
    unlock = counter_to_str(keys, counter)
    value = int(unlock)

    final_mod = value % 3
    if final_mod != 0:
        mod1 = None
        mod2 = []

        for num_text in reversed(unlock):
            num = int(num_text)
            current_mod = num % 3

            if current_mod == final_mod:
                mod1 = num_text
                break
            elif current_mod != 0:
                mod2.append(num_text)
        
        if mod1:
            counter[mod1] -= 1
        elif mod2:
            counter[mod2[0]] -= 1
            counter[mod2[1]] -= 1

        unlock = counter_to_str(keys, counter)

    return unlock


if __name__ == '__main__':
    lock = input().strip()
    unlock = solve(lock)
    print(unlock)