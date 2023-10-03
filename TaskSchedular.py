'''
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. 
Tasks could be done in any order. Each task is done in one unit of time. 
For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), 
that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.
Example 2:

Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
'''
from typing import List
from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        maxHeap = [-cnt for cnt in counter.values()]
        queue = deque()
        tasks_time = 0
        while maxHeap or queue:
            tasks_time +=1
            if not maxHeap:
                tasks_time = queue[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt !=0:
                    queue.append([cnt, tasks_time + n])
                
            if queue and queue[0][1] == tasks_time:
                heapq.heappush(maxHeap,queue.popleft()[0])
        

        return tasks_time

 


obj = Solution()
tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2
print("total time ->", obj.leastInterval(tasks,n))
