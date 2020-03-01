#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the weightedUniformStrings function below.
# Easy

dic = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26}
def weightedUniformStrings(s, queries):
    sum_letter = 0
    num_dic = dict()
    for i,v in enumerate(s):
        if i == 0:
            sum_letter = dic.get(v)
            num_dic[sum_letter] = sum_letter
        else:
            if v == s[i-1]:
                sum_letter += dic.get(v)
            else:
                sum_letter = dic.get(v)
            num_dic[sum_letter] = sum_letter
    print(num_dic)
                
    result = []
    for num in queries:
        try:
            num_dic[num]
            result.append("Yes")
        except:
            result.append("No")

    return result




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

