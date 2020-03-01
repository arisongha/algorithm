#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the separateNumbers function below.
# Easy

def separateNumbers(s):
    def isVal(s, first):
        while s:
            if s.startswith(first):
                s = s[len(first):]
                first = str(int(first) + 1)
            else:
                return False
        return True

    if s[0] == '0' and len(s) > 1:
        print("NO")
        return
    else:
        for ind in range(1, len(s)//2 + 1):
            first = s[:ind]
            if isVal(str(s), first):
                print("YES " + first)
                return

        print("NO")
        return

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)

