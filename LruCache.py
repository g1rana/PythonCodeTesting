class Node:
    def __init__(self,key,val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LruCache:
    def __init__(self,capacity):
        self.capacity = capacity
        self.cache = {}
        self.head= Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add_node(self,node):
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node
    
    def _remove_node(self,node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        node.next , node.prev = None, None
    
    def _move_to_end(self,node):
        self._remove_node(node)
        self._add_node(node)

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.move_to_end(node)
            return node.val
        return -1
    
    def put(self,key,val):
        if key in self.cache:
            node=self.cache[key]
            node.val = val
            self.move_to_end(node)
        else:
            if len(self.cache)>= self.capacity:
                del_node = self.head.next
                self._remove_node(del_node)
                del self.cache[del_node.key]

            node = Node(key,val)
            self._add_node(node)