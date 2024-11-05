from collections import deque
def bfs(i,j, maps, n, m):
    res = 0
    q = deque()
    q.append([i,j])
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    while q:
        x,y = q.popleft()
        
        if maps[x][y] == "X":
            continue
            
        res += int(maps[x][y])
        maps[x][y] = 'X'
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx <0 or nx > n-1 or ny < 0 or ny > m-1:
                continue
            if maps[nx][ny].isdigit():
                q.append([nx,ny])
    
    return res
        

def solution(maps):
    tmp = []
    n = len(maps)
    m = len(maps[0])
    
    maps = list(map(lambda x : list(x), maps))

    for i in range(n):
        for j in range(m):
            if maps[i][j]!='X':
                tmp.append(bfs(i,j, maps, n, m))
    return [-1] if tmp == [] else sorted(tmp)           
                
                
