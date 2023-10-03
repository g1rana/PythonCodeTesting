'''
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. 
If it is impossible to reach a Gate, that room should remain filled with INF
'''
from typing import List
from collections import deque
INF = 2**31 -1
def walls_and_gates(rooms: List[List[int]]):
    #RUN BFS walks from all possible gates to find its nearest empty rooms
    q = deque()
    rows = len(rooms)
    cols = len(rooms[0])
    seen = set()
    for r in range(rows):
        for c in range(cols):
            if rooms[r][c] == 0:
                #found gate add into queue for initial walk
                q.append([r,c])
    # directions = [[1,0],[-1,0],[0,1],[0,-1]]
    def addRoom(r,c):
        if (r < 0 or r == rows or c < 0 or c==cols or (r,c) in seen or rooms[r][c] == -1):
            return 
        q.append([r,c])
        seen.add((r,c))
    dist = 0
    while q:
        for _ in range(len(q)):
            r,c = q.popleft()
            rooms[r][c] = dist
            addRoom(r+1,c)
            addRoom(r,c+1)
            addRoom(r-1,c)
            addRoom(r,c-1)
        
        dist +=1


rooms_1 = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
room_2 = [[0,-1],[2147483647,2147483647]]

print("Room1->", walls_and_gates(rooms_1), f"Rooms_1:{rooms_1}")
print("Room2->", walls_and_gates(room_2), f"Rooms_2:{room_2}")



