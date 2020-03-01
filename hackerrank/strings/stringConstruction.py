#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stringConstruction function below.
# Easy

def stringConstruction(s):
    dics = dict()
    for i,v in enumerate(s):
        dics[v] = dics.get(v, 0) + 1
        
    return len(dics)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = stringConstruction(s)

        fptr.write(str(result) + '\n')

    fptr.close()

