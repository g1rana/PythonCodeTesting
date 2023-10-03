#Time complexity O(V + E) and space complexity O(V)

def topSort(g):
    visited = set()
    visiting = set()
    topOrder = list()
    for vertex in g:
        if vertex not in visited:
            topSortUtil(g,vertex,visited,set(),[],topOrder)
    topOrder.reverse()

def topSortUtil(g, v, visited,pathSet,path,topOrder):
    if v in pathSet:
        raise Exception("found cycle as path")
    if v in visited:
        return
    pathSet.add(v)
    visited.add(v)
    path.append(v)
    for neig in g[v]:
        topSortUtil(g,neig, visited,pathSet,path,topOrder)
    topOrder.append(v)
    pathSet.remove(v)
    path.pop()