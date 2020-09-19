from random import randint
import os
import sys
from os.path import join
from v3 import main

test_folder = sys.argv[1]

start = len(os.listdir(join(test_folder, 'inp'))) + 1

number_of_new_test = 1

for i in range(start, start + number_of_new_test):
    inp = open(join('inp', str(i)), 'w')
    out = open(join('out', str(i)), 'w')

    n = 1000
    k = 1_000_000_000
    result = main(n, k)

    inp.write(str(n) + ' ' + str(k))
    out.write(str(result) + '\n')

    inp.close()
    out.close()
