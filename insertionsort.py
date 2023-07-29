#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    val = arr[-1]
    j = n- 2
    if n == 1: print(*arr)
    else:
        while arr[j] >val and j >=0:
            arr[j + 1]= arr[j]
            j -= 1
            print(*arr)
        arr[j + 1] = val
        print(*arr)
    
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
