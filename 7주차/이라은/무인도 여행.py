from collections import deque 
  
def solution(maps):
    answer = []
    # 세로, 가로
    height = len(maps)
    width = len(maps[0])
    
    visited = [[False] * width for _ in range(height)]
    
    q = deque()
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    def bfs(y,x,count):
        while q:
            nowy, nowx = q.popleft()
            for i in range(4):              
                nx = nowx + dx[i]
                ny = nowy + dy[i]
                if 0 <= nx < width and 0 <= ny < height:
                    if maps[ny][nx] != 'X' and not visited[ny][nx]:
                        visited[ny][nx] = True
                        count += int(maps[ny][nx])
                        q.append((ny, nx))
        return count
    
    for j in range(height):
        for i in range(width):
            if maps[j][i] != 'X' and not visited[j][i]:
                visited[j][i] = True
                q.append((j,i)) 
                answer.append(bfs(j,i,int(maps[j][i])))
    
    answer.sort()
    if not answer:
        answer = [-1]
    return answer
