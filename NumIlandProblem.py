def getNumILand(matrix):
    visitid = [ [0 for c in range(len(matrix))] for r in range(len(matrix))]
    print(visitid)
    row = len(matrix)
    col = len(matrix)
    count = 0

    for r in range(row):
        for c in range(col):
            if visitid[r][c] == 0 and matrix[r][c] == 1:
                dfsWalk(matrix,r,c,visitid)
                count +=1
    return count



def getNeigh(matrix,r,c,visited):
    dir = [(0,1),(0,-1),(-1,0),(1,0)]
    neig = []
    for d in dir:
        x = r + d[0]
        y = c + d[1]
        if x >=0 and y <= len(matrix) and matrix[x][y] == 1 and visited[x][y] == 0:
            neig.append((x,y))
    return neig
    
def dfsWalk(matrix,r,c,visited):
    if visited[r][c] == 1:
        return
    neig = getNeigh(matrix,r,c,visited):
    for n in neig:
        dfsWalk(matrix,n[0],n[1],visited)






if __name__ == "__main__":
    matrix = [[0,0,0,1], [1,0,1,1],[0,1,1,1],[1,0,0,1]]
    getNumILand(matrix)