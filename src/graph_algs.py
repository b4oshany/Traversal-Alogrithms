"""Algorithms for processing graphs discussed in lectures and tutorials"""

import Queue
import graph
import traversal

import forest

def dfs(g, u):
    """Visit all the nodes of g, starting from u, in a DFS manner"""
    result = traversal.Traversal(g)
    dfsVisit(g, u, result)
    for v in g.nodes():
        if not result.isVisited(v):
            dfsVisit(g, v, result)
    return result

def dfsVisit(g, u, result):
    """DFS visit connnected component of g containing u, starting from u"""
    # result.markStart(u)
    result.visit(u)
    for v in g.nbrs(u):
        if not result.isVisited(v):
            result.discover(v, u)
            # do anything related to edge (u,v)
            dfsVisit(g, v, result)
    result.markFinish(u)

def bfs(g, u):
    """Perform a BFS on g starting from u"""
    result = traversal.Traversal(g)
    # implement the process here
    bfsVisit(g, u, result)
    return result

def bfsVisit(g, u, result):
    result.visit(u)
    cn = []
    for v in g.nbrs(u):
        if not result.isVisited(v):
            result.discover(v, u)
            result.visit(v)
            cn.append(v)  
    result.markFinish(u)
    for a in cn:
       bfsVisit(g, a, result)
    
        
        
        
        
