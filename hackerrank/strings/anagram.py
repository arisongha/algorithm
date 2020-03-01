#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the anagram function below.
# Easy

def anagram(s):
    if len(s) % 2 != 0:
        return -1
    dic1 = dict()
    dic2 = dict()
    for i, v in enumerate(s[:len(s)//2]):
        dic1[v] = dic1.get(v, 0) + 1
    for i, v in enumerate(s[len(s)//2:]):
        dic2[v] = dic2.get(v, 0) + 1
    
    count = 0
    for k,v in dic1.items():
        if dic2.get(k) and v-dic2[k]>=0:
            count += v-dic2[k]
        elif dic2.get(k) == None:
            count += v
        
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()

