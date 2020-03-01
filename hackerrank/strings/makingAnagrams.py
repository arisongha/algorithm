#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makingAnagrams function below.
# Easy

def makingAnagrams(s1, s2):
    dic1 = dict()
    dic2 = dict()
    for i, v in enumerate(s1):
        dic1[v] = dic1.get(v, 0) + 1
    for i, v in enumerate(s2):
        dic2[v] = dic2.get(v, 0) + 1
    
    count = 0
    for k,v in dic1.items():
        if dic2.get(k):
            count += min(dic1[k], dic2[k])
            
    sums1 = sum(dic1.values())
    sums2 = sum(dic2.values())
    
    return sums1 + sums2 - count*2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()

