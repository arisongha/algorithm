#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
# Medium

def isValid(s):
    if len(s) == 1:
        return "YES"
    temp_dic = dict()
    for i,v in enumerate(s):
        temp_dic[v] = temp_dic.get(v, 0) + 1
    if len(set(list(temp_dic.values()))) == 1:
        return "YES"
        
    for k,v in temp_dic.items():
        copy_dic = temp_dic.copy()
        copy_dic[k] = v-1
        if copy_dic.get(k) == 0:
            copy_dic.pop(k, 0)
            if len(set(list(copy_dic.values()))) == 1:
                return "YES"
            else:
                return "NO"
        else:
            print("else: {}".format(copy_dic))
            if len(set(list(copy_dic.values()))) == 1:
                return "YES"
    return "NO"
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()

