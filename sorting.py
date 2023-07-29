#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    swapcnt = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                a[i] , a[j] = a[j] , a[i]
                swapcnt += 1
    first = a[0]
    last = a[-1]
    print(f'Array is sorted in {swapcnt} swaps.')
    print(f'First Element: {first}')
    print(f'Last Element: {last}')
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
