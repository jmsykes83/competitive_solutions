#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    lst = [0,0,0]
    for el in set(arr):
        if el > 0:
            lst[0] += arr.count(el)
        elif el < 0:
            lst[1] += arr.count(el)
        elif el == 0:
            lst[2] += arr.count(el)
    # print("set",set(arr))
    # print("list",lst)
    print(f"{lst[0]/len(arr):.6f} \n{lst[1]/len(arr):.6f} \n{lst[2]/len(arr):.6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
