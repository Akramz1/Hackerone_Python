#!/bin/python3
from datetime import datetime
import math
import os
import random
import re
import sys

# Complete the time_delta function below.


def time_delta(t1, t2):
    formt = '%a %d %b %Y %H:%M:%S %z'
    dt1 = datetime.strptime(t1, formt)
    dt2 = datetime.strptime(t2, formt)
    ans = abs(int((dt1-dt2).total_seconds()))
    return str(ans)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
