#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gemstones function below.
# Easy

def gemstones(arr):
    set_list = []
    for ar in arr:
        temp_set = set()
        for s in ar:
            temp_set.add(s)
        set_list.append(temp_set)
    
    set_sum = []
    for set_ in set_list:
        set_sum += list(set_)
    for set_ in set_list:
        set_sum = set(set_sum).intersection(set_)
    
    return len(set_sum)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

