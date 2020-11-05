import os
import sys
import subprocess
from time import perf_counter
from os import listdir
from os.path import join

try:
    from natsort import natsorted as sorted
except ImportError:
    pass


def report(
        filename,
        input_text,
        user_output_text,
        correct_output_text,
        user_runtime,
        runtime_limit,
        is_rte,
        is_tle,
        verbose=False
):
    """Print test results to screen"""

    if is_rte:
        return_code = 'RTE'
    elif is_tle:
        return_code = 'TLE'
    elif user_output_text == correct_output_text:
        return_code = 'PASS'
    else:
        return_code = 'FAILED'

    mark = '✅'
    if return_code != 'PASS':
        mark = '❌'

    report_text = []

    _MAX_LEN = 42
    _SPACES = 9

    report_text.append('{}\n'.format('-' * _MAX_LEN))
    report_text.append()
    test_filename = 'TEST {}: '.format(filename)
    len_so_far = len(test_filename)

    padding1 = _MAX_LEN - len(test_filename) - _SPACES
    report_text.append('{}{}'.format(' ' * padding1, return_code))

    padding2 = _SPACES - len(return_code) - 2

    report_text.append(' ' * padding2)

    report_text.append('{}\n'.format(mark))

    # Additional information
    if verbose:
        report_text.append('Input\n{}\n'.format(input_text))
        report_text.append('Correct output\n{}\n'.format(correct_output_text))

        if return_code not in ['TLE']:
            report_text.append('Your output\n{}\n'.format(user_output_text))
            report_text.append("Correct output's length: {}\n".format(len(correct_output_text)))
            report_text.append("Your    output's length: {}\n".format(len(user_output_text)))

        if return_code != 'RTE':
            report_text.append('\nRan in {:.3f} s\n'.format(user_runtime))

    print(''.join(report_text), end='')


if __name__ == '__main__':

    try:
        f = open(sys.argv[1])
    except FileNotFoundError:
        print(sys.argv[1] + ' not found')
        raise
    f.close()

    python_file = sys.argv[1]

    test_folder = sys.argv[2]

    try:
        time_limit = float(sys.argv[3])
    except IndexError:
        time_limit = None
    except ValueError:
        time_limit = None

    is_verbose = False
    if sys.argv[-1] == '-v':
        is_verbose = True

    num_inputs = len(os.listdir(os.path.join(test_folder, 'inp')))

    command = ['python', python_file]

    # Run tests and report
    inp_files_name = sorted(listdir(join(test_folder, 'inp')))
    for test_id in inp_files_name:
        inp = open(join(test_folder, 'inp', test_id))
        out = open(join(test_folder, 'out', test_id))

        correct_output = out.read()

        rte = False
        tle = False
        start = perf_counter()
        try:
            process_output = subprocess.run(
                command,
                stdin=inp,
                check=True,
                text=True,
                capture_output=True,
                timeout=time_limit
            ).stdout
        except subprocess.CalledProcessError as exc:
            rte = True
            process_output = exc.stderr
        except subprocess.TimeoutExpired:
            tle = True
            process_output = ''

        process_runtime = perf_counter() - start

        inp.seek(0)
        test_input = inp.read()

        report(
            test_id,
            test_input,
            process_output,
            correct_output,
            process_runtime,
            time_limit,
            rte,
            tle,
            is_verbose
        )

        inp.close()
        out.close()
