from collections import Counter

def sorted_counter_to_str(sorted_keys, counter):
    string = []

    for key in sorted_keys:
        string.append(key * counts[key])

    return ''.join(string)


if __name__ == '__main__':
    lock = input()

    counts = Counter(lock)

    keys = sorted(counts.keys(), reverse=True)

    unlock = sorted_counter_to_str(keys, counts)

    while int(unlock) % 3 != 0:
        mod = int(unlock) % 3
        for key in reversed(keys):
            if int(key) % 3 == mod:
                counts[key] -= 1
                break

        keys = sorted(counts.keys(), reverse=True)
        unlock = sorted_counter_to_str(keys, counts)


    print(unlock)