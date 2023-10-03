class Node(object):
    def __init__(self,v=None):
        self.val = v
        self.neig = []

class build_other_graph(node):
    new_graph = {}
    self.dfs(node)
    return new_graph[node.val]
    def dfs(self,node,new_graph):
        tmp = Node(node.val)
        new_graph[node.val] = tmp
        for neig in node.neig:
            if neig.val not in new_graph:
                self.dfs(node,new_graph)
            new_graph[neig.val].neig.append(tmp)
        


