import io
import sys
import subprocess

def convert_to_lf(string):
    return string.replace("\r\n", "\n").replace("\r", "\n")

if __name__ == '__main__':
    input_file = open(sys.argv[2])
    output_file = open(sys.argv[3])

    num_test_case = int(input_file.readline())
    num_line_each_test_input = int(input_file.readline()) 
    num_line_each_test_output = int(input_file.readline()) 


    cases = []
    for _ in range(num_test_case):
        case = ''
        for i in range(num_line_each_test_input):
            case += input_file.readline()
        cases.append(case)


    command = ['python', sys.argv[1]]

    print('-' * 30)
    process_output = ''

    for i in range(num_test_case):
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        raw_process_output = process.communicate(bytes(cases[i], 'ascii'))[0].decode()
        process_output = convert_to_lf(raw_process_output)

        correct_output = ''
        for j in range(num_line_each_test_output):
            correct_output += convert_to_lf(output_file.readline())
        
        print('TEST {}: '.format(i + 1), end='')

        if process_output == correct_output:
            print('PASS   ✅')
        else:
            print('FAILED ❌')
            print('Correct output')
            print(correct_output)
            print('Your output')
            print(process_output)

        print('-' * 30)
