#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    N = len(a)
    options = [0]*100
    for x in a:
        options[x]+=1
    threes = [sum(options[i:(i+2)]) for i in range(len(options)-1)]
    # the longest chain is the number 
    print(threes)
    return max(threes)

    # the longest chain is the longest chain a[:-1] (+1 if a[-1] can attach to it)
    # If more than one chains are longest choose the one a[-1] can attach to
    # longests = helper(a)
    # print(longests)
    # return max([len(x) for x in longests])

def helper(a):
    if len(a)==1:
        return [a]
    longests = helper(a[:-1])
    longests = sorted(longests, key=lambda x: len(x), reverse=True)
    new_longests = []
    attached = False
    for longest in longests:
        diff = abs(longest[-1]-a[-1])
        if diff==0:
            new_longests.append(longest+[a[-1]])
            attached = True
            continue
        if diff==1:
            new_longests.append(longest+[a[-1]])            
            attached = True
        new_longests.append(longest)
    if not attached:
        new_longests.append([a[-1]])
    return new_longests


if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    print(str(result) + '\n')

#    fptr.close()

