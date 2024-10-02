from collections import deque
import sys

c,r=map(int,input().split())
graph=[]
visited=[[False]*c for _ in range(r)]
tomato=deque([])
for i in range(r):
    tmp=list(map(int, sys.stdin.readline().strip().split()))
    for j in range(c):
        if tmp[j]==1:
            tomato.append([0,i,j])
    graph.append(tmp)

time=-1
while tomato:
    time,a,b=tomato.popleft()
    # print(time,a,b)
    time+=1
    if visited[a][b]:
        continue
    visited[a][b]=True
    for i,j in [[1,0],[-1,0],[0,1],[0,-1]]:
        nx=a+i
        ny=b+j
        # print(nx,ny)
        if 0<=nx<r and 0<=ny<c:
            if graph[nx][ny]==0:
                graph[nx][ny]=1
                tomato.append([time,nx,ny])

# print(time-1)
for g in graph:
    if 0 in g:
        print(-1)
        break
else:
    print(time-1)


