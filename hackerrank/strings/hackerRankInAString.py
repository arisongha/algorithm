#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
# Easy
 
def hackerrankInString(s):
    hackerrank = "hackerrank"
    for char in s:
        if char == hackerrank[0]:
            if len(hackerrank) == 1:
                return "YES"
            else:
                hackerrank = hackerrank[1:]
    return "NO"
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()

