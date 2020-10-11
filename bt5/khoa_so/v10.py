def solve(lock: str) -> str:
    # if remainder_of_lock != 0
    # redundants[0] stores the number that satisfies 
    # this equation redundants[0] % 3 == remainder_of_lock
    # redundants[1], redundants[2] stores numbers that satisfy
    # this equation (redundants[1] + redundants[2]) % 3 == remainder_of_lock
    inf = 10
    redundants = [inf, inf, inf]
    remainder_of_lock = int(lock) % 3

    counter = [0 for _ in range(10)]

    for num in lock:
        num = int(num)
        counter[num] += 1
        remainder_of_num = num % 3

        if remainder_of_lock == 0 or remainder_of_num == 0:
            continue

        if remainder_of_lock == remainder_of_num:
            i = 0
        elif redundants[1] > redundants[2]:
            i = 1
        else:
            i = 2
            
        if num < redundants[i]:
            redundants[i] = num

    if inf != redundants[0]:
        counter[redundants[0]] -= 1
    elif inf not in redundants[1:3]:
        counter[redundants[1]] -= 1
        counter[redundants[2]] -= 1

    unlock = []
    for num in reversed(range(10)):
        unlock.append(str(num) * counter[num])

    return ''.join(unlock)


if __name__ == '__main__':
    lock = input().strip()
    unlock = solve(lock)
    print(unlock)
# old version
