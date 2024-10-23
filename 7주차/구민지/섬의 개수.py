from collections import deque
import sys

dx=[0,0,1,-1,1,-1,-1,1]
dy=[1,-1,0,0,1,-1,1,-1]

def bfs(x,y):
    global graph,visited,w,h
    if visited[x][y] or graph[x][y]==0:
        return 0
    cnt=0
    q=deque([[x,y]])
    while q:
        a,b=q.popleft()
        if visited[a][b]:
            continue
        visited[a][b]=True
        for i,j in zip(dx,dy):
            nx,ny=a+i,b+j
            if 0<=nx<h and 0<=ny<w:
                if not visited[nx][ny] and graph[nx][ny]:
                    q.append([nx,ny])
    return 1


while True:
    w,h=map(int,input().split())
    if w==0 and h==0:
        break
    graph=[]
    island_cnt=0
    for _ in range(h):
        graph.append(list(map(int,sys.stdin.readline().strip().split())))
    visited=[[False]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if bfs(i,j):
                island_cnt+=1
    print(island_cnt)
