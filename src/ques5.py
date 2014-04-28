"""Module to test the functionality of the BFS and DFS traversals, and
 display the respective trees."""

import random
from graph_algs import dfs, bfs
import graph

def test():
    g = graph.Graph({'a':['b', 'g', 'd'], 'b':['c', 'd'], 'c':['f', 'a'],
                     'd':['g', 'f'], 'e':['d', 'g', 'h'], 'f':['e', 'b'], 'g':['f', 'h'], 'h':['f', 'a']})
    print "Graph: %s" % g.nbhds
    print "Running DFS..."
    dt = dfs(g, 'a')
    dt.printTree()
    dt.showTree()
    print "Running BFS..."
    bt = bfs(g, 'a')
    bt.printTree()
    bt.showTree()
    #print "Traversals completed!"

if __name__ == '__main__':
    test()
