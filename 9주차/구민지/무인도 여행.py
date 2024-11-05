from collections import deque 
        
def solution(maps):
    answer = []
    
    visited=[[False]*len(maps[0]) for _ in range(len(maps))]
    def bfs(x,y):
        if visited[x][y] or maps[x][y]=="X":
            return 0
        total=0
        q=deque([[x,y]])
        while q:
            x,y=q.popleft()
            if visited[x][y]:
                continue
            visited[x][y]=True
            total+=int(maps[x][y])
            for i,j in [[1,0],[0,1],[0,-1],[-1,0]]:
                nx,ny=x+i,y+j
                if 0<=nx<len(maps) and 0<=ny<len(maps[0]):
                    if maps[nx][ny]!="X" and not visited[nx][ny]:
                        q.append([nx,ny])
        return total
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            rtn=bfs(i,j)
            if rtn:
                answer.append(rtn)
    if not answer:
        return [-1]
    return sorted(answer)
