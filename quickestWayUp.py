#!/bin/python3

import math
import os
import random
import re
import sys

class Node(object):
    def __init__(self, i):
        self.i = i
        self.neighbors = []

    def __repr__(self):
        return str(self.i)+'->'+','.join([str(node.i) for node in self.neighbors])

def create_graph(ladders, snakes):
    g = [None]*101
    for i in range(100,0,-1):
        node = Node(i)
        node.neighbors = [g[i+j] for j in range(1,7) if i+j<=100]
        g[i] = node
    for f,t in ladders+snakes:
        for j in range(1,7):
            if f-j>0:
                g[f-j].neighbors.remove(g[f])
                g[f-j].neighbors.append(g[t])
    return g

def bfg(g, f, t):
    level = 0
    q = [g[f],level]
    visited = set()
    while True:
        node = q.pop(0)
        if type(node)==int:
            level += 1
            q.append(level)
            continue
        if node.i==t:
            return level
        visited.add(node)
        for neighbor in node.neighbors:
            if neighbor in visited:
                continue
            q.append(neighbor)
        
# Complete the quickestWayUp function below.
def quickestWayUp(ladders, snakes):
    # create a directed graph where the nodes are the squares from 1 to 100 and the edges are either from the node to the 6 next nodes or to the end of the ladder/snake if applicable.
    g = create_graph(ladders, snakes)
    # print(g)
    # bfg to find the smallest amount of hops to node 100
    return bfg(g, 1, 100)

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        ladders = []

        for _ in range(n):
            ladders.append(list(map(int, input().rstrip().split())))

        m = int(input())

        snakes = []

        for _ in range(m):
            snakes.append(list(map(int, input().rstrip().split())))

        result = quickestWayUp(ladders, snakes)

        print(str(result) + '\n')


