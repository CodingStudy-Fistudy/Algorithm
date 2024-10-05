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

                
#2차원리스트 1차원으로 변환해서, 0이 있는지 체크            
res = sum(graph,[])

#0이 리스트에 하나도 없는 경우 0출력하고 프로그램 종료
if 0 not in res:
    print(0)
    exit(0)
#0이 리스트에 존재하는 경우 좌표를 다 돌면서 1인 좌표값을 덱에 추가
else:    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                queue.append([i,j])
                
bfs()

#2차원리스트 1차원으로 변환해서, 0이 있는지 체크 
res_2 = sum(graph, [])
#0이 있다면 변환하지 못하는 부분이 있으므로 -1출력하고 프로그램 종료
if 0 in res_2:
    print(-1)
    exit(0)
else:
    print(max(res_2)-1)
                

    


                



    

