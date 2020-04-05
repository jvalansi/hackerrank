#!/bin/python3

import os
import sys

#
# Complete the waiter function below.
#
def waiter(number, q):
    #
    # Write your code here.
    #
    A = number[::-1]
    B = []
    new_A = []
    p = 2
    print('A: {}'.format(A))
    print('B: {}'.format(B))
    for i in range(q):
        B.append([])
        for x in A:
            if x%p:
                new_A.insert(0,x)
            else:
                B[-1].insert(0,x)
        A = new_A
        new_A = []
        p = next_prime()
        print('A: {}'.format(A))
        print('B: {}'.format(B))
    return [x for B_i in B for x in B_i] + A

primes = [2]

def next_prime():
    i = primes[-1]
    while not is_prime(i):
        i+=1
    primes.append(i)
    return i

def is_prime(i):
    for p in primes:
        if i%p==0:
            return False
    return True

if __name__ == '__main__':

    with open('input.txt') as f:
        data = f.read()
    nq = data.split()

    n = int(nq[0])

    q = int(nq[1])

    number = list(map(int, nq[2:]))

    result = waiter(number, q)

    print('\n'.join(map(str, result)))
    print('\n')

    #fptr.close()

