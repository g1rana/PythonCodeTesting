'''
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) 
connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.


'''
#logic to find island with maximum number of cells
from typing import List
def findMaxAreaIsland(grid:List[List[int]]) ->int:
    rows = len(grid)
    cols = len(grid[0])
    seen = set()
    dirs=[(1,0),(-1,0),(0,-1),(0,1)]
    def dfs(r:int,c:int):
        if r not in range(rows) or c not in range(cols) or (r,c) in seen or grid[r][c] == 0:
            return 0
        count = 1
        seen.add((r,c))
        for dx,dy in dirs:
            count += dfs(r+dx,c+dy)
        return count
    
    maxArea = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r,c) not in seen:
                area = dfs(r,c)
                maxArea = max(maxArea,area)
    return maxArea

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

print("MaxAread->",findMaxAreaIsland(grid))