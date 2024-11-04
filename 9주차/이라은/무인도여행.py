from collections import deque

def solution(maps):
    answer = []
    graph = []
    
    for i in range(len(maps)):
        graph.append(list(maps[i]))

    visited = [[False] * len(graph[0]) for _ in range(len(graph))]
    q = deque()
    cnt_lst = []
    
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    def bfs(x,y,cnt):
        q.append((x,y))
        cnt += int(graph[x][y])
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]) and not visited[nx][ny] and graph[nx][ny] != 'X':
                    visited[nx][ny] = True
                    cnt += int(graph[nx][ny])
                    q.append((nx,ny))
        cnt_lst.append(cnt)
        return

    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] != 'X' and not visited[i][j]:
                visited[i][j] = True 
                bfs(i,j,0)
    
    if cnt_lst:
        cnt_lst.sort()
    else:
        cnt_lst.append(-1)
    return cnt_lst
