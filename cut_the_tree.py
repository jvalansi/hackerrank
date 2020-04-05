#!/bin/python3

import math
import os
import random
import re
import sys

used = set()
edge_dict = {}
class Node(object):
    def __init__(self, index, value):
        self.index = index
        self.value = value
        self.children = []
        self.total = 0

    def add_children(self, nodes):
        used.add(self.index)
        for child_index in edge_dict[self.index]:
            if child_index in used: 
                continue
            child = nodes[child_index]
            self.children.append(child)
            child.add_children(nodes)


def build_tree(data, edges):
    nodes = [None]+[Node(i+1, value) for i, value in enumerate(data)]
    for i,j in edges:
        if i not in edge_dict:
            edge_dict[i] = []
        edge_dict[i].append(j)
        if j not in edge_dict:
            edge_dict[j] = []
        edge_dict[j].append(i)
    print(edge_dict)
    root = nodes[1]
    root.add_children(nodes)
    return root


def calc_sub(tree):
    tree.total = tree.value
    for child in tree.children:
        tree.total += calc_sub(child)
    return tree.total

def find_sub(tree, target):
    closest_sub = tree.total
    for child in tree.children:
        child_closest_sub = find_sub(child, target)
        closest_sub = closest_sub if abs(target-closest_sub)<abs(target-child_closest_sub) else child_closest_sub
    return closest_sub


# Complete the 'cutTheTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY data
#  2. 2D_INTEGER_ARRAY edges
#

def cutTheTree(data, edges):
    # Write your code here
    # build tree
    tree = build_tree(data,edges)
    # calc sub tree sums - bottom up
    calc_sub(tree)
    # find sub tree that sums closest to total_sum/2
    closest_sub = find_sub(tree, tree.total/2)
    # return 2*(total_sum/2-sum)
    return abs(int(2*(tree.total/2-closest_sub)))

if __name__ == '__main__':

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    edges = []

    for _ in range(n - 1):
        edges.append(list(map(int, input().rstrip().split())))

    result = cutTheTree(data, edges)

    print(str(result) + '\n')


