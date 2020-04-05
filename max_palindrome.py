#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
from copy import copy
import math
from functools import reduce
from operator import mul
MOD=1000000007
#
# Complete the 'initialize' function below.
#
# The function accepts STRING s as parameter.
#
counts = []
factorials = [1]
inverses = [1]
def initialize(s):
    # This function is called once before all queries.
    d = {}
    counts.append(Counter(d))
    i=0
    for c in s:
        # print(c)
        if c not in d:
            d[c] = 0
        d[c]+=1
        counts.append(Counter(d))
        factorial = (factorials[i]*(i+1))%MOD
        factorials.append(factorial)
        inverse = exp_by_squaring(factorial,MOD-2)%MOD
        inverses.append(inverse)
        i+=1
    print(factorials)

def exp_by_squaring(x, n):
    # print(n)
    # print(x)
    if n < 0:   return exp_by_squaring(1 / x, -n)
    elif n == 0:  return  1
    elif n == 1:  return  x
    elif n%2==0: return exp_by_squaring((x * x)%MOD,  n // 2)
    elif n%2==1: return x * exp_by_squaring((x * x) %MOD, (n - 1) // 2)


#
# Complete the 'answerQuery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#

def answerQuery(l, r):
    # Return the answer for this query modulo 1000000007.
    # the number of palindromes in a string is the number of permutations
    # of the letters that appear more than once.
    # times the number of residue characters.
    sub_counts = counts[r] - counts[l-1]
    wing_letters = {k: v//2 for k,v in sub_counts.items()}
    center_letters = {k: v%2 for k,v in sub_counts.items()}
    wing_vals = wing_letters.values()
    wing_len = sum(wing_vals)
    nom = factorials[wing_len]
    # print(nom)
    denom = reduce(mul ,map(inverses.__getitem__, wing_vals))
    # print(denom)
    centers = sum(center_letters.values())
    # print(centers)
    return (nom * denom * max(1,centers))%1000000007

def get_factorial(n):
    N = len(factorials)
    if N>n:
        return factorials[n]
    for i in range(N-1,n):
        res = factorials[i]*(i+1)
        factorials.append(res)
    return res

if __name__ == '__main__':

    s = input()

    print('initialize')
    initialize(s)
    print('done')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        l = int(first_multiple_input[0])

        r = int(first_multiple_input[1])

        result = answerQuery(l, r)

        print(str(result) + '\n')

