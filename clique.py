#!/bin/python3

import math
import os
import random
import re
import sys
import bisect
from math import floor
from functools import partial
#
# Complete the 'clique' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

    # The Turán graph T(n,k) is defined as the unique graph without a (k+1)-clique having the maximum possible number of graph edges, namely:
def max_edges_wo_clique(k):
    return floor(((k-1)*(n**2))/(2*k))



def clique(n, m):
    # Write your code here
    def binary_search(lo, hi, tgt):
        if (hi-lo)<=1:
            return hi if max_edges_wo_clique(lo) < tgt else lo
        mid = lo + (hi-lo)//2
        T_n_k = max_edges_wo_clique(mid)
        if T_n_k <= tgt:
            return binary_search(mid, hi, tgt)
        if T_n_k > tgt:
            return binary_search(lo, mid, tgt)

    return binary_search(1, n+1, m)
    i=1
    while max_edges_wo_clique(i)<m:
        i+=1
    return i
    

if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = clique(n, m)

        print(str(result))


