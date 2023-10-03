'''
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
'''
from typing import List
from collections import deque 
def orangesRotting(grid: List[List[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    fresh=times=0
    q = deque() 
    #find all rotten orange and put them in queue for start
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                fresh +=1
            if grid[r][c] == 2:
                q.append([r,c])
    directions = [[1,0],[-1,0],[0,1],[0,-1]]
    while q and fresh > 0:
        for _ in range(len(q)):
            r,c = q.popleft()
            for dx,dy in directions:
                dx , dy = dx +r, dy+c
                if (
                        dx in range(len(grid))
                        and dy in range(len(grid[0]))
                        and grid[dx][dy] == 1
                    ):
                    grid[dx][dy] == 2
                    q.append([dx,dy])
                    fresh -=1

        times +=1
    
    return times if fresh == 0 else -1

grid_1 = [[2,1,1],[1,1,0],[0,1,1]]
grid_2 = [[2,1,1],[0,1,1],[1,0,1]]
grid_3 = [[0,2]]


print(f"Grid:{grid_1} result: {orangesRotting(grid_1)}")
print(f"Grid:{grid_2} result: {orangesRotting(grid_2)}") 
print(f"Grid:{grid_3} result: {orangesRotting(grid_3)}")  