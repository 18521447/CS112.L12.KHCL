from random import randint

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
            num_list.pop(mod2_indices[0])
            num_list.pop(mod2_indices[1])

    return ''.join(num_list)

start = 11
for i in range(start, start + 20):
    inp = open('inp/' + str(i), 'w')
    out = open('out/' + str(i), 'w')

    inp_text = []
    for i in range(randint(3, 10**5)):
        inp_text.append(str(randint(0, 9)))

    inp_text = ''.join(inp_text)
    inp.write(inp_text)
    out_text = solve(inp_text) + '\n'
    out.write(out_text)