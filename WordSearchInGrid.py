'''
Given an m x n grid of characters board and a string word, 
return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells,
 where adjacent cells are horizontally or vertically neighboring.
   The same letter cell may not be used more than once.

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
'''
from typing import List
def exist(board: List[List[str]], word: str) -> bool:
    m = len(board)
    n = len(board[0])
    nei_cells = [(1,0),(-1,0),(0,1),(0,-1)]
    def dfs(r,c,idx: int, word: str)->bool:
        #Base Case 
        if idx == len(word):
            return True
        
        #Business logic, 
        #Non-match or grid out of bound case
        if (r < 0 or r > m-1 or c < 0 or c > n-1 or board[r][c] != word[idx]):
            return False
        
        #Means (r.c) cell match with word at index idx
        #repurpose grid (r,c) cell temporarily with '#'
        board[r][c] = '#'
        for dx,dy in nei_cells:
            if dfs(r+dx,c+dy,idx+1,word):
                return True
        
        board[r][c] = word[idx]
        
        return False
    
    for r in range(m):
        for c in range(n):
            if board[r][c] == word[0]:
                if dfs(r,c,0,word):
                    return True
    return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "ABCCED"
word = "ABCB"
print(exist(board,word))