'''
Merge Two sorted link-list :

'''
class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

def mergeSortedLinkList(list1:ListNode, list2:ListNode)->ListNode:
    dummy = ListNode()
    cur = dummy
    while(list1 and list2):
        if list1.val < list2.val:
            cur.next = list1
            list1 = list1.next
        else:
            cur.next = list2
            list2= list2.next
        cur = cur.next
    if list2:
        cur.next=list2
    elif list1:
         cur.next =list1
    return dummy.next

'''
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
L0->L1->L2
L0 - L1->L2 -> L0 - > L2->L1 - Merged = L0->L2->L1
L0-L1 - Slow ->L1,
'''
def reorderList(head:ListNode) ->ListNode:
    #find middle
    slow,fast = head,head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    #reverse second half
    second = slow.next
    prev = slow.next = None
    while(second):
        tmp = second.next
        second.next = prev
        prev = second
        second = tmp
    #merge two half
    first , second = head, prev
    while(second):
        tmp1,tmp2 = first.next,second.next
        first.next = second
        second.next = tmp1
        first ,second = tmp1, tmp2


'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
'''
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0,head)
    left,right = dummy, head
    #move nth to right 
    while(n > 0):
        n -=1
        right = right.next
    #Now left and right are n node part
    while(right):
        left = left.next
        right = right.next
    
    # at this stage , left and right are n+1 node apart
    left.next = left.next.next
    return dummy.next

'''
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.
'''
def copyRandomList(self, head: ListNode) -> ListNode:
    oldToCopy = {None:None}
    #first pass: Copy original node into hashMap
    cur = head
    while cur:
        clone = ListNode(cur.val)
        oldToCopy[cur] = clone
        cur = cur.next
    #second pass: Now adjust pointer in copyNode to build deep copylist
    cur = head
    while cur:
        copy = oldToCopy[cur]
        copy.next = oldToCopy[cur.next]
        copy.random = oldToCopy[cur.random]
        cur = cur.next
    
    return oldToCopy[head]

'''
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself. 
Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
'''
def SumListNode(l1:ListNode,l2:ListNode) ->ListNode:
    dummy = ListNode()
    carry = 0
    cur = dummy
    while l1 or l2 or carry:
        sum = carry
        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next

        carry = sum // 10
        cur.next = ListNode(sum%10)
        cur = cur.next
    return dummy.next
        


'''
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

'''

class Node:
    def __init__(self,key,val):
        self.key,self.val= key,val
        self.next=self.prev = None
    

class LruCache:
    def __init__(self,capacity):
        self.capacity = capacity
        self.cache = {} #key to node
        self.left,self.right=Node(0,0),Node(0,0)
        self.left.next,self.right.prev = self.right, self.left
    
    #add Node into before tail
    def add_node(self,node):
        next,prev = self.right , self.right.prev
        prev.next=next.prev = node
        node.next,node.prev = next,prev
    #remove node
    def remove_node(self,node):
        next,prev = node.next, node.prev
        prev.next, next.prev = next,prev
    
    def get(self,key):
        if key in self.cache:
            self.remove_node(self.cache[key])
            self.add_node(self.cache[key])
            return self.cache[key].val
        return -1
    def put(self,key,val):
        if key in self.cache:
            self.remove_node(self.cache[key])
        
        self.cache[key] = Node(key,val)
        self.add_node(self.cache[key])
        if len(self.cache) > self.capacity:
            #remove from front of list
            lru = self.left.next
            self.remove_node(lru)
            del self.capacity[lru]


'''
Same LRU cache Using OderedDict module of python
''' 
from collections import OrderedDict
class LruCache:
    def __init__(self,capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
    
    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
    def put(self,key,val):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = val
        if len(self.cache) >= self.capacity:
            items = self.cache.popitem(last=False)
            print("Lru itesm->", "key->",items[0],"val->",items[1])

# cache = LruCache(3)
# print("Set key", 'A')
# cache.put('A',26)
# print("Set key", 'B')
# cache.put('B',27)
# print("GETt key", 'A')
# cache.get('A')
# print("Set key", 'C')
# cache.put('C',28)
# print("Set key", 'D')
# cache.put('D',29)
# print("GETt key", 'C')
# cache.get('C')
# print("Set key", 'E')
# cache.put('E',30)

'''
287. Find the Duplicate Number
Medium
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
 

Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
'''
from typing import List 
def findDuplicate(self,nums:List[int]) ->int:
    slow=fast = 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast: break

    slow=0
    while True:
        slow = nums[slow]
        fast = nums[fast]
        if slow == fast:
            return slow
        

'''
Find Median value of order stream of integers(seen so far) at given time 
'''
#Divided seen stream of interger into 2 half 
#1- First half contain all element from middle which value is smaller then middle -> MaxHeap
#2 - Second half contain all elements whoes value is greater then middle  ---> MinHeap
#Since python don't have in module support for max heap library therefore implementing Max heap using
# inserting element with its negative value . 
# Algo-
# Always inserts new stream integer into first in maxheap then rebalance if diffrence between 2 heap > 1

import heapq
class findMedian:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
    
    def add_nums(self,nums:int):
        #First Insert Element In first half of which contain small elements half
        heapq.heappush(self.maxHeap,-nums)
        #then move higest element to second half.
        heapq.heappush(self.minHeap,-heapq.heappop(self.maxHeap))
        #whenever , first half is smaller then second half then move min element to maxheap
        if len(self.minHeap) > len(self.maxHeap):
            heapq.heappush(self.maxHeap,-heapq.heappop(self.minHeap))
   
    def get_median(self) ->float:
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0])/2
        return -self.maxHeap[0]
    
median = findMedian()
median.add_nums(1)
median.add_nums(17)
median.add_nums(10)
median.add_nums(6)
median.add_nums(4)
median.add_nums(2)
median.add_nums(9)
# print("Get Median :-?", median.get_median())
# 1-2-4-6-9-10-17
# -max -4 -7
# - min -1
'''
703. Kth Largest Element in a Stream
Companies
Design a class to find the kth largest element in a stream. Note that it is the kth
largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:
KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
'''
import heapq
class KthLargets:
    def __init__(self,k:int, nums:List[int]):
        self.size = k
        self.heap = nums 
        heapq.heapify(self.heap)
        while len(self.heap) > k : 
            heapq.heappop(self.heap)
    
    def add(self,val:int) ->int:
        heapq.heappush(self.heap,val)
        if len(self.heap) > self.size:
            heapq.heappop(self.heap)
        return self.heap[0]
    
kthLargest = KthLargets(3, [4, 5, 8, 2])
print(kthLargest.add(3))   # return 4
print(kthLargest.add(5))  # return 5
print(kthLargest.add(10))  # return 5
print(kthLargest.add(9))   # return 8
print((kthLargest.add(4)))   # return 8

'''
1046. Last Stone Weight
You are given an array of integers stones where stones[i] is the weight of the ith stone.
We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.

Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
'''
def findLastStoneWeight(stones:List[int]) ->int:
    stones = [-stone for stone in stones] #Prepare for Max Heap , since pyhton heapq only support min prirority queue
    #therefore storing stone value in negative 

    heapq.heapify(stones)
    while len(stones) > 1:
        x = abs(heapq.heappop(stones))
        y = abs(heapq.heappop(stones))
        if x != y: 
            heapq.heappush(stones,-(y-x))

    return -stones[0] if len(stones) != 0 else 0

stones = [2,7,4,1,8,1]

print("Higest weight stones:->",findLastStoneWeight(stones))

'''
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k,
return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).


You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
'''
#Using minHeap logic
def findKClosestPointsFromOrigin(points:List[int],k:int) ->List[List[int]]:
    minHeap = []
    #O(N)time complexity for appending element in minheap
    for x,y in points:
        dist = x**2 + y**2
        minHeap.append([dist,x,y])

    #Run heapify,which it takes  O(N) operation to convert given array into actual minHeap
    heapq.heapify(minHeap)
    #After heapify , pop items k times from minheap to get k closest points from origin
    
    #which klog(n) operation
    res = []
    while k > 0:
        _,x,y = heapq.heappop(minHeap)
        k -=1
        res.append([x,y])
    return res

points = [[3,3],[5,-1],[-2,4]]
k = 2
print("K closest points:->",findKClosestPointsFromOrigin(points,k))


'''
Parse the file concurrently:
1- Read file in chuck 
2- And run each chunks through woker for wokre's pool
3- Concatnate result of reach 
'''
import concurrent.futures

def parse_the_log():
    return

def parse_log_file_concurrently():
    logfile_path = "my.text"
    chunk = 1000
    
    with open(logfile_path,'r') as logfile:
        chunks = [logfile.readlines(chunk) for _ in range(chunk) ]

        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as excutor:
            result = list(excutor.map(parse_the_log,chunks))




