import io
import sys
import subprocess

if __name__ == '__main__':
    input_file = open(sys.argv[2])
    correct_output = open(sys.argv[3])

    num_test_case = int(input_file.readline())
    num_line_each_test_case = input_file.read().count('\n') // num_test_case

    input_file.seek(0)
    input_file.readline()

    cases = []
    for _ in range(num_test_case):
        case = ''
        for i in range(num_line_each_test_case):
            case += input_file.readline()
        cases.append(case)


    command = ["python", sys.argv[1]]

    process_output = ''
    for i in range(num_test_case):
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        process_output = process.communicate(bytes(cases[i], 'ascii'))[0].decode()
        result = 'Pass   ✅' if process_output == correct_output.readline() else 'Failed ❌'
        print("Test #{}: {}".format(i + 1, result))
