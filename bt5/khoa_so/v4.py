from collections import Counter

def sorted_counts_to_str(sorted_keys, counter):
    string = []

    for key in sorted_keys:
        string.append(key * counter[key])

    return ''.join(string)


if __name__ == '__main__':
    lock = input().strip()

    counts = Counter(lock)
    keys = sorted(counts.keys(), reverse=True)

    unlock = sorted_counts_to_str(keys, counts)
    value = int(unlock)

    if value % 3 != 0:
        final_mod = value % 3
        current_mod = 0

        for num_text in reversed(unlock):
            num = int(num_text)

            if num % 3 == 0:
                continue
            if current_mod == final_mod:
                break

            counts[num_text] -= 1
            current_mod += num
            current_mod %= 3       
        
        keys = sorted(counts.keys(), reverse=True)
        unlock = sorted_counts_to_str(keys, counts)

    print(unlock)