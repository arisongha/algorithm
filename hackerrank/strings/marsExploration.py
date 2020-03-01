#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
# Easy

def marsExploration(s):
    sos_cnt = len(s) // 3
    sos = "SOS" * sos_cnt
    result = 0 
    for a,b in zip(s,sos):
        if a is not b:
            result += 1
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()

