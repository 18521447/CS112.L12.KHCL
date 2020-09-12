import io
import sys
import subprocess

if __name__ == '__main__':
    input_file = open(sys.argv[2])
    output_file = open(sys.argv[3])

    num_test_case = int(input_file.readline())
    num_line_each_test_input = input_file.read().count('\n') // num_test_case
    num_line_each_test_output = output_file.read().count('\n') // num_test_case

    input_file.seek(0)
    input_file.readline()
    output_file.seek(0)

    cases = []
    for _ in range(num_test_case):
        case = ''
        for i in range(num_line_each_test_input):
            case += input_file.readline()
        cases.append(case)


    command = ["python", sys.argv[1]]

    process_output = ''
    for i in range(num_test_case):
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        process_output = process.communicate(bytes(cases[i], 'ascii'))[0].decode()

        correct_output = ''
        for j in range(num_line_each_test_output):
            correct_output += output_file.readline()
        result = 'Pass   ✅' if process_output == correct_output else 'Failed ❌'
        print("Test #{}: {}".format(i + 1, result))
