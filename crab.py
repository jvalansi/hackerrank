#!/bin/python3

import os
import sys

class Node(object):
    def __init__(self, n):
        self.n = n
        self.neighbors = {}
        self.feet = 0

    def copy(self):
        n = Node(self.n)
        n.neighbors = self.neighbors.copy()
        n.feet = self.feet
        return n


class Graph(object):
    def __init__(self, edges=[], t=None):
        self.nodes = {}
        self.t = t
        self.crabs = 0
        for edge in edges:
            self.insert_edge(edge)

    def walk(self, edge=None):
        vertex = edge[0] if edge else 1
        q = [vertex]
        visited = [edge]
        while q:
            node = q.pop()
            for neighbor in self.nodes[node].neighbors:
                if [neighbor, node] in visited or [node, neighbor] in visited:
                    continue
                q.append(neighbor)
                visited.append([node, neighbor])
                yield [node, neighbor]

    def insert(self, node):
        if node not in self.nodes:
            self.nodes[node] = Node(node)

    def insert_edge(self, edge):
        v0, v1 = edge
        self.insert(v0)
        self.insert(v1)
        self.nodes[v0].neighbors[v1] = self.nodes[v1]
        self.nodes[v1].neighbors[v0] = self.nodes[v0]

    def violates_rules(self, edge):
        v0, v1 = edge
        if (self.nodes[v0].feet <= self.t) and (self.nodes[v1].feet == 1):
            print("False")
            return False
        if (self.nodes[v1].feet <= self.t) and (self.nodes[v0].feet == 1):
            print("False")
            return False
        print("True")
        return True

    def turn_on(self, edge):
        v0, v1 = edge
        self.insert_edge(edge)
        self.nodes[v0].feet += 1
        self.nodes[v1].feet += 1
        self.crabs += self.nodes[v0].feet==1
        self.crabs += self.nodes[v1].feet==1

    def turn_off(self, edge):
        v0, v1 = edge
        self.nodes[v0].feet -= 1
        self.nodes[v1].feet -= 1
        self.crabs -= self.nodes[v0].feet==0
        self.crabs -= self.nodes[v1].feet==0

    def copy(self):
        g = Graph()
        g.nodes = {k: v.copy() for k,v in self.nodes.items()}
        g.t = self.t
        g.crabs = self.crabs
        return g

    def __str__(self):
        s = ""
        for node in self.nodes:
            s += "{}: {}, ".format(node, self.nodes[node].feet)
        return s
#
# Complete the crabGraphs function below.
#
def crabGraphs(n, t, graph):
    #
    # Write your code here.
    #

    # dp - 
    # grow the graph edge by edge. for each edge keep the best graph with and without it.
    # for the next edge, check all neighboring visited edges, and take the best graph without it and the best graph with it (restriction - must connect to head)
    
    # try to grow the graph edge by edge, 
    # for each edge:
        # check every other edge, if violates the rules turn of, else turn on
    # if the graph is better with the edge, keep it on, else turn off
    graph = Graph(graph)
    crab_graph = Graph(t=t)
    num_crabs = 0
    for edge in graph.walk():
        print(edge)
        tmp_graph = crab_graph.copy()
        tmp_graph.turn_on(edge)
        for edge_ in tmp_graph.walk(edge):
            if tmp_graph.violates_rules(edge_):
                tmp_graph.turn_off(edge_)
        if tmp_graph.crabs > num_crabs:
            num_crabs = tmp_graph.crabs
            crab_graph = tmp_graph
        print(crab_graph)
    return num_crabs
    


if __name__ == '__main__':

    c = int(input())

    for c_itr in range(c):
        ntm = input().split()

        n = int(ntm[0])

        t = int(ntm[1])

        m = int(ntm[2])

        graph = []

        for _ in range(m):
            graph.append(list(map(int, input().rstrip().split())))

        result = crabGraphs(n, t, graph)

        print(str(result) + '\n')


