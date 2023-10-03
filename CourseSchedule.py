'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take 
course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
'''
from typing import List
from collections import defaultdict,deque
def canFinish(numCourses:int, prerequisites:List[List[int]]) ->bool:
    indegree= defaultdict(int)
    coursesMap = defaultdict(list)
    for a,b in prerequisites:
        indegree[a] +=1
        coursesMap[b].append(a)

    q = deque()
    for i in range(numCourses):
        #find all courses which don't depended on any other courses
        if i not in indegree:
            q.append(i)

    while q :
        for _ in range(len(q)):
            course = q.popleft()
            for nei in coursesMap[course]:
                indegree[nei] -=1
                if indegree[nei] == 0:
                    q.append(nei)
                    del indegree[nei]
    
    return True if len(indegree) == 0 else False


numCourses = 2
prerequisites_1 = [[1,0]]

numCourses = 2
prerequisites_2 = [[1,0],[0,1]]

print("Output{prerequisites_1}:", canFinish(2,prerequisites_1))
print("Output{prerequisites_2}:", canFinish(2,prerequisites_2))

