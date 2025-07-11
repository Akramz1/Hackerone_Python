#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.


def solve(s):
    s2 = list(s)
    s2[0] = s2[0].upper()
    for i in range(len(s2)):
        if s2[i] == ' ':
            s2[i+1] = s2[i+1].upper()
    return ''.join(s2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
