#Graph could be valid Tree with following condition
#1- Graph is not having any Cycle -> Detecting Cycle logic in non-directed graph using preVNode 
#
#2- Graph is single connected graph means there shouldn't be more than 1 connect
# component of graph

'''
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), 
write a function to check whether these edges make up a valid tree.

You can assume that no duplicate edges will appear in edges.
 Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
'''
from typing import List
from collections import defaultdict
def valid_tree(n: int, edges: List[List[int]]) -> bool:
    #Empty Graph is Valid Tree
    if not n:
        return True
    graph = defaultdict(list)

    #Build Adjancency List
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)


    #DFS walk to find if is there any Cycle
    def dfs(node,visit,parent):
        if node in visit:
            return False
        visit.add(node)
        for nei in graph[node]:
            if nei == parent:
                continue
            if not dfs(nei,visit,node):
                return False
        return True
    
    visit = set()
    #start from starting node
    # End check if Graph don't have Cycle
    if not dfs(0,visit,-1): 
        return False
    
    #Now, Check graph is single connected graph
    return len(visit) == n

n = 5 
edges_1 = [[0, 1], [0, 2], [0, 3], [1, 4]]
edges_2 = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]


print("n=?", n, "edge->",edges_1)
print("Is  Graph with  Edge_1 Tree ?",valid_tree(5,edges_1))
print("Is Graph with Edge_2 Tree ?",valid_tree(5,edges_2))


'''
You have a graph of n nodes. You are given an integer n and an array edges 
where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.
Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
'''
def countComponent(n:int, edges:List[List[int]]) ->int:
    graph = defaultdict(list)
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visit = set()

    def dfs(node):
        if node not in visit:
            visit.add(node)
            for nei in graph[node]:
                dfs(nei)
        return
    connect_count =0 

    for i in range(n):
        if i not in visit:
            dfs(i)
            connect_count +=1
    return connect_count

n = 5
edges = [[0,1],[1,2],[3,4]]
edges_2 = [[0,1],[1,2],[2,3],[3,4]]

print("connect component->",countComponent(n,edges))
print("connect component->",countComponent(n,edges_2))


'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest 
path from the root node down to the farthest leaf node.
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root:TreeNode) ->int:
    if not root:
        return root
    left =maxDepth(root.left)
    right =maxDepth(root.right)
    return max(left , right) + 1

'''
Given the root of a binary tree, invert the tree, and return its root.
'''
def invertTree(root:TreeNode):
    if not root: return root
    left =  invertTree(root.right)
    right =  invertTree(root.left)
    root.left = right 
    root.right = left
    return root
'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
'''
def isSameTree(p,q:TreeNode) ->bool:
    if not p and not q: return True
    if not p or not q: return False
    if p.val != q.val: return False
    return isSameTree(p.left,q.left) and isSameTree(p.right,q.right) 


'''
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure 
and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. 
The tree tree could also be considered as a subtree of itself.
'''

def isSubTree(root:TreeNode, subTree:TreeNode) ->bool:
    if not root and not subTree : return True
    if not root :return False
    if isSameTree(root,subTree): return True
    return isSubTree(root.left, subTree) or isSubTree(root.right, subTree) 

'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q 
as the lowest node in T that has both p and q as descendants 
(where we allow a node to be a descendant of itself).”
'''
def lowestCommonBSTAncestor(root:TreeNode,p:TreeNode,q:TreeNode) ->TreeNode:
    cur = root
    while cur:
        if  p.val > cur.val and q.val > cur.val:
            cur = cur.right
        elif p.val < cur.val and q.val < cur.val:
            cur = cur.left
        else:
            return cur
        
        




