
import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
# Easy

char_dict = dict()
def superReducedString(s):
    count = 0
    while len(s) != count:
        count = 0
        for char in s:
            if char*2 in s:
                s = s.replace(char*2, "")
                continue
            else:
                count += 1
        
    result = ""
    if len(s) == 0:
        result = "Empty String"
    else:
        result = s
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()

