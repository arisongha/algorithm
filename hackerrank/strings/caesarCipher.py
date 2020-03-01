
import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
# Easy

original = "abcdefghijklmnopqrstuvwxyz"
rotated = ""
alphabet_dict = dict()
def caesarCipher(s, k):
    k = k % 26
    rotated = original[k:] + original[:k]
    for o,r in zip(original, rotated):
        alphabet_dict[o] = r
        alphabet_dict[o.upper()] = r.upper()

    result = ""
    for char in s:
        if char.isalpha():
            result += alphabet_dict[char]
        else:
            result += char
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()

