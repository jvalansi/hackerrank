#!/bin/python3

import os
import sys
from copy import copy
from collections import Counter
from fractions import Fraction
import time
#
# Complete the storyOfATree function below.
#
class Node(object):
    def __init__(self, i):
        self.i = i
        self.neighbors = set()
        self.correct = None

    def __repr__(self):
        return str(self.i)

def build_graph(n,edges):
    g = [None]*(n+1)
    for i,j in edges:
        if g[i] is None:
            g[i] = Node(i)
        if g[j] is None:
            g[j] = Node(j)
        g[i].neighbors.add(g[j])
        g[j].neighbors.add(g[i])
    return g


all_correct_roots = {}
def storyOfATree(n, edges, k, guesses):
    #
    # Write your code here.
    #
    # build graph
    g = build_graph(n,edges)
    guesses = set(tuple(guess) for guess in guesses)
    # traverse graph to find current correct guesses
    start = time.time()
    correct = get_correct(g[1], guesses, set())
    end = time.time()
    print(end - start)
    # print(correct)
    # traverse graph keeping track of correct guesses by flipping correctness when traversing an edge
    start = time.time()
    success = keep_track(g[1], guesses, correct, set())
    end = time.time()
    print(end - start)
    # print(all_correct)
    # success = 0
    # for correct in all_correct:
    #     success += len(correct)>=k
    f = Fraction(success, n)
    return "{}/{}".format(f.numerator, f.denominator)


def keep_track(node, guesses, correct, visited):
    q = [node]
    node.correct = correct
    success = 0
    while q:
        node = q.pop(0)
        success += len(node.correct)>=k
        visited.add(node)
        for neighbor in node.neighbors:
            if neighbor in visited:
                continue
            visited.add(neighbor)
            q.append(neighbor)
            new_correct = copy(node.correct)
            if (node.i, neighbor.i) in guesses:
                new_correct.remove((node.i,neighbor.i))
            if (neighbor.i, node.i) in guesses:
                new_correct.add((neighbor.i, node.i))
            neighbor.correct = new_correct
            # all_correct.extend(keep_track(neighbor, guesses, new_correct, visited))
    return success

def get_correct(node, guesses, visited):
    correct = set()
    q = [node]
    while q:
        node = q.pop(0)
        visited.add(node)
        for neighbor in node.neighbors:
            if neighbor in visited:
                continue
            visited.add(neighbor)
            q.append(neighbor)
            if (node.i, neighbor.i) in guesses:
                correct.add((node.i,neighbor.i))
            # correct |= get_correct(neighbor, guesses, visited)
    return correct

def solve_with_correct_roots(g, edges, k, guesses):
    get_all_correct_roots(g, edges)
    # print(all_correct_roots)
    # for each guess
    m = Counter()
    for i,guess in enumerate(guesses):
        # get all the roots where the guess is correct
        correct_roots = all_correct_roots[tuple(guess)]
        c = Counter(correct_roots)
        m += c
    # print(m)
    # for each root
    success = 0
    for i in range(1,n+1):
        # check sum correct guess >= k
        success += m[i]>=k
    # return success/n
    f = Fraction(success, n)
    return "{}/{}".format(f.numerator, f.denominator)


def get_all_correct_roots(g, edges):
    # the correct roots for edge (i,j) is the sum of correct roots of all edges from i except (i,j)
    for i,j in edges:
        all_correct_roots[(i,j)] = get_correct_roots(g, i, j)
        all_correct_roots[(j,i)] = set(range(1,n+1)) - all_correct_roots[(i,j)]

def get_correct_roots(g, i, j):
    if (i,j) in all_correct_roots:
        return all_correct_roots[(i,j)]
    correct_roots = set([i])
    for node in g[i].neighbors:
        if node.i == j:
            continue
        correct_roots |= get_correct_roots(g, node.i, i)
    return correct_roots

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        edges = []

        for i,_ in enumerate(range(n-1)):
            edges.append(list(map(int, input().rstrip().split())))

        gk = input().split()

        g = int(gk[0])

        k = int(gk[1])

        guesses = []

        for i,_ in enumerate(range(g)):
            guesses.append(list(map(int, input().rstrip().split())))

        result = storyOfATree(n, edges, k, guesses)

        print(result + '\n')


