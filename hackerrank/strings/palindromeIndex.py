#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the palindromeIndex function below.
# Easy

def isPalindrome(s):
    for idx in range(len(s)//2):
        if s[idx] != s[len(s)-idx-1]:
            return False
    return True
 
def palindromeIndex(s):
    for idx in range((len(s)+1)//2):
        if s[idx] != s[len(s)-idx-1]:
            if isPalindrome(s[:idx]+s[idx+1:]):
                return idx
            else:
                return len(s)-idx-1
    return -1



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()

