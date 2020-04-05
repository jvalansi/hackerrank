#!/bin/python3

import os
import sys
import time

# Complete the solve function below.
def solve(shots, players):
    # all_numbers = list(set(sorted([i for pair in shots+players for i in pair])))
    starts,ends = zip(*shots)
    shots_starts = sorted([(start,i) for i,start in enumerate(starts)])
    shots_ends = sorted([(end,i) for i,end in enumerate(ends)])
    starts,ends = zip(*players)
    players_starts = sorted([(start,i) for i,start in enumerate(starts)])
    players_ends = sorted([(end,i) for i,end in enumerate(ends)])

    start = time.time()
    before_end_dict=get_before_end_dict(players_ends, shots_starts)
    after_start_dict=get_after_start_dict(players_starts, shots_ends)
    print(time.time()-start)

    start = time.time()
    s = get_s(shots_starts, shots_ends, before_end_dict, after_start_dict)
    print(time.time()-start)
    return s

def get_s(shots_starts, shots_ends, before_end_dict, after_start_dict):
    s=0
    starts,shots0 = zip(*shots_starts)
    ends,shots1 = zip(*shots_ends)
    for i in range(len(players)):
        before_end = shots0[:before_end_dict[i]]
        after_start = shots1[after_start_dict[i]+1:]
        si = set(before_end).intersection(set(after_start))
        s+=len(si)
    return s

def get_before_end_dict(players_ends, shots_starts):
    j=0 
    before_end_dict={}
    for end,i in players_ends:
        while j<len(shots_starts) and shots_starts[j][0]<=end:
            j+=1
        before_end_dict[i] = j
    return before_end_dict

def get_after_start_dict(players_starts, shots_ends):
    j=len(shots_ends)-1
    after_start_dict={}
    for start,i in players_starts[::-1]:
        while j>=0 and shots_ends[j][0]>=start:
            j-=1
        after_start_dict[i] = j
    return after_start_dict


if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    shots = []

    for _ in range(n):
        shots.append(list(map(int, input().rstrip().split())))

    players = []

    for _ in range(m):
        players.append(list(map(int, input().rstrip().split())))

    result = solve(shots, players)

    print(str(result) + '\n')

