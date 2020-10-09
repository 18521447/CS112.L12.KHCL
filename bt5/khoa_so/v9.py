def solve(lock: str) -> str:
    INF = 10
    goal_mod = int(lock) % 3

    counter = [0 for _ in range(10)]
    mod1 = INF
    mod2 = [INF, INF]
    for num in map(int, list(lock)):
        counter[num] += 1
        
        current_mod = num % 3
        if goal_mod == 0 or current_mod == 0:
            continue
        
        if current_mod == goal_mod and num < mod1:
            if mod1 != INF:
                counter[mod1] += 1
            counter[num] -= 1
            if mod2[0] != INF:
                counter[mod2[0]] += 1
                mod2[0] = INF
            if mod2[1] != INF:
                counter[mod2[1]] += 1
                mod2[1] = INF
            mod1 = num
        elif mod1 == INF:
            max_index = 0 if mod2[0] > mod2[1] else 1
            if num < mod2[max_index]:
                if mod2[max_index] != INF:
                    counter[mod2[max_index]] += 1
                counter[num] -= 1
                mod2[max_index] = num

    unlock = []
    for i in reversed(range(10)):
        unlock.append(str(i) * counter[i])

    return ''.join(unlock)


if __name__ == '__main__':
    lock = input().strip()
    unlock = solve(lock)
    print(unlock)