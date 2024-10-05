#7576번 백준 토마토
from collections import deque

m,n = map(int, input().split())
warn = -1


graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))
    
queue = deque([])
    
dx = [-1,1,0,0]
dy = [0,0,-1,1]

#bfs 함수 정의            
def bfs():
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
                
            if nx <0 or ny < 0 or nx > n-1 or ny > m-1:
                continue
            if graph[nx][ny] == -1:
                continue
                
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y]+1
                queue.append([nx,ny])
          
            
res = sum(graph,[])

#0이 리스트에 하나도 없는 경우 0리턴
if 0 not in res:
    print(0)
    exit(0)
else:
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                queue.append([i,j])
                

bfs()
#print(graph)
res_2 = sum(graph, [])
if 0 in res_2:
    print(-1)
    exit(0)
else:
    print(max(res_2)-1)
