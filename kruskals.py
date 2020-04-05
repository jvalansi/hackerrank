#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kruskals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#

class Component(object):
    def __init__(self, i):
        self.i = i
        self.members = set([i])

    def __repr__(self):
        return str(self.i)

def update(components, f, t):
    cf = components[f]
    ct = components[t]
    for member in ct.members:
        components[member] = cf
    cf.members |= ct.members

def kruskals(g_nodes, g_from, g_to, g_weight):
    # Write your code here
    edges = zip(g_weight, g_from, g_to)
    edges = sorted(edges)
    print(edges)
    componenets = {node: Component(node) for node in range(1, g_nodes+1)}
    s = 0
    for w, f, t in edges:
        print(componenets)
        if componenets[f] == componenets[t]:
            continue
        update(componenets, f, t)
        s += w
    return s

if __name__ == '__main__':

    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    res = kruskals(g_nodes, g_from, g_to, g_weight)

    # Write your code here.
    print(str(res))


