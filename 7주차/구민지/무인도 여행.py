from collections import deque 

dx=[0,0,1,-1]
dy=[1,-1,0,0]

visited=[]
r,c=0,0
maps=[]
def bfs(x,y):
    global visited,maps,r,c
    cnt=0
    if visited[x][y] or maps[x][y]=='X':
        return 0
    q=deque([[x,y]])
    while q:
        a,b=q.popleft()
        if visited[a][b]:
            continue
        cnt+=int(maps[a][b])
        visited[a][b]=True
        for i,j in zip(dx,dy):
            nx,ny=a+i,b+j
            if 0<=nx<r and 0<=ny<c:
                if not visited[nx][ny] and maps[nx][ny]!='X':
                    q.append([nx,ny])
    return cnt
        
def solution(mapz):
    answer = []
    global visited,maps,r,c
    for m in mapz:
        maps.append(list(m))
    r,c=len(maps),len(maps[0])
    visited=[[False]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            tmp=bfs(i,j)
            if tmp:
                answer.append(tmp)
    if answer:
        return sorted(answer)
    else:
        return [-1]
