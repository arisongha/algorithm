#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the theLoveLetterMystery function below.
# Easy

def theLoveLetterMystery(s):
    n = len(s)
    count = 0
    for i in range(n // 2):
        left = ord(s[i])
        right = ord(s[(n - 1) - i])
        if left != right:
            count += abs(right - left)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()


