
def solve(lock: str) -> str:
    num_list = sorted(lock, reverse=True)
    unlock = ''.join(num_list)
    final_mod = int(unlock) % 3

    if final_mod != 0:
        mod1_index = None
        mod2_indices = []

        for i in reversed(range(len(num_list))):
            num = int(num_list[i])
            current_mod = num % 3

            if current_mod == final_mod:
                mod1_index = i
                break
            elif current_mod != 0 and len(mod2_indices) < 2:
                mod2_indices.append(i)
        
        if mod1_index:
            num_list.pop(mod1_index)
        elif mod2_indices:
            num_list.pop(mod2_indices[0])
            num_list.pop(mod2_indices[1])

        unlock = ''.join(num_list)
    return unlock


if __name__ == '__main__':
    lock = input().strip()
    unlock = solve(lock)
    print(unlock)