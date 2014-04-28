"""Module to test the functionality of the BFS and DFS traversals, and
 display the respective trees."""

import random
from graph_algs import dfs, bfs
import graph

def test():
    g = graph.Graph({'a':['b', 'c', 'd'], 'b':['c', 'e', 'f'], 'c':['d', 'e'],
                     'd':['b', 'f'], 'e':['a'], 'f':['c', 'a']})
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
