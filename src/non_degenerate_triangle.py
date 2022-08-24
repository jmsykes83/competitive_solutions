#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

def maximumPerimeterTriangle(sticks):
    # Write your code here
    triangle = [-1]
    ordered_sticks = sorted(sticks, reverse=True)
    for i in range(len(ordered_sticks)-2):
        side_one = ordered_sticks[i+1]
        side_two = ordered_sticks[i+2]
        if ordered_sticks[i] >= side_one + side_two:
            continue
        return [side_two,side_one,ordered_sticks[i]]
    return triangle
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
