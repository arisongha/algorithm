#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pangrams function below.
# Easy

def pangrams(s):
    lower_s = s.lower().replace(" ","")
    alpha_dict = dict()
    for char in lower_s:
        alpha_dict[char] = alpha_dict.get(char, 0) + 1
    if len(alpha_dict) == 26:
        return "pangram"
    else:
        return "not pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()

