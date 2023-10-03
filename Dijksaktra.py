from queue import PriorityQueue
class Graph(object):
    def __init__(self):
        self.v 
        self.neig = {} # neigh stored as hash map where key as neigh and values as weigh
                        # as value in hash map

def dijkestra(Graph,start):
    dist = {start: 0}
    visited = set()
    pq = PriorityQueue()
    pq.put((0,start))
    back_ref = {start: None}
    while not pq.empty():
        p,v = pq.get()
        visited.add(v)
        for neig, w in v.neig.items():
            if neig not in visited:
                if dist[v] + w < dist.get(neig,default=float("inf")):
                    dist[neig] = dist[v] + w
                    pq.put(dist[neig],neig)
                    back_ref[neig] = v
                    



