import io
import sys
import subprocess
from  subprocess import PIPE

if __name__ == '__main__':

    try: 
        open(sys.argv[1])
    except FileNotFoundError:
        print(sys.argv[1] + ' not found')
        raise
    finally:
        python_file = sys.argv[1]

    try:
        input_file = open(sys.argv[2])
    except FileNotFoundError:
        print(sys.argv[2] + ' not found')
        raise

    try:
        output_file = open(sys.argv[3])
    except FileNotFoundError:
        print(sys.argv[3] + ' not found')
        raise

    inputs = input_file.read().split('---\n')
    num_inputs = len(inputs)
    correct_outputs = output_file.read().split('---\n')

    command = ['python', python_file]

    print('-' * 30)
    process_output = ''

    for i in range(num_inputs):
        process_output = subprocess.Popen(command, stdin=PIPE, stdout=PIPE, text=True).communicate(inputs[i])[0]
        
        print('TEST {}: '.format(i + 1), end='')

        if process_output == correct_outputs[i]:
            print('PASS')
        else:
            print('FAILED')
            print('Correct output')
            print(correct_outputs[i])
            print('Your output')
            print(process_output)
            print('Correct output\'s length:', len(correct_outputs[i]))
            print('Your    output\'s length:', len(process_output))
            

        print('-' * 30)
