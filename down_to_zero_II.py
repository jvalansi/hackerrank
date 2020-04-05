#!/bin/python3

import os
import sys

#
# Complete the downToZero function below.
#
def downToZero(n):
    #
    # Write your code here.
    #
    return step(n)

steps = [0,1]
def step(n):
    if len(steps)>n:
        return steps[n]
    get_max_dividers()
    with open('max_dividers.json', 'w') as f:
        import pandas as pd
        pd.to_csv(max_dividers)
        json.dump(max_dividers, f)
    for j in range(len(steps), n+1):
        a = max_dividers[j] if j in max_dividers else None
        prev_steps = min(steps[j-1],steps[a]) if a else steps[j-1]
        steps.append(prev_steps+1)
    # print(steps)
    return steps[n]

max_dividers = {}
def get_max_dividers():
    if max_dividers:
        return
    for i in range(2,int(10**6)+1):
        i_ = int(10**6/i)
        for j in range(2,min(i,i_)+1):
            max_dividers[i*j]=i if i*j not in max_dividers or max_dividers[i*j]>i else max_dividers[i*j]
    

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = downToZero(n)

        print(str(result) + '\n')

