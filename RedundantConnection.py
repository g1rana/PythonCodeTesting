'''
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n,
 with one additional edge added. The added edge has two different vertices chosen from 1 to n, 
 and was not an edge that already existed. The graph is represented as an array edges of length n 
 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. 
If there are multiple answers, return the answer that occurs last in the input.
'''
from typing import List
from collections import defaultdict
def findRedundantConnection(edges:List[List[int]]) ->List[int]:
    graph = defaultdict(list)

    def isLoop(s,t,seen)->bool:
        if s not in seen:
            seen.add(s)
            if s == t: return True
            for n in graph[s]:
                if isLoop(n,t,seen): return True
        return False
    for u, v in edges:
        seen = set()
        #if u in graph and v in graph and isLoop(u,v,seen):
        if isLoop(u,v,seen):
            return [u,v]
        graph[u].append(v)
        graph[v].append(u)
    

edges_1 = [[1,2],[1,3],[2,3]]
edges_2 = [[1,2],[2,3],[3,4],[1,4],[1,5]]
print("Edage->",findRedundantConnection(edges_1))
print("Edage->",findRedundantConnection(edges_2))



