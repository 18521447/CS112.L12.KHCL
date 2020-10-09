
def solve(lock: str) -> str:
    num_list = sorted(lock, reverse=True)
    final_mod = int(lock) % 3

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
            num_list = [num_list[i] for i in range(len(num_list)) if i not in mod2_indices]

    return ''.join(num_list)


if __name__ == '__main__':
    lock = input().strip()
    unlock = solve(lock)
    print(unlock)