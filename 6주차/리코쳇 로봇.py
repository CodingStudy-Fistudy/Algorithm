from collections import deque

def solution(board):
 
    answer = 0
    N = len(board)
    M = len(board[0])
    q = deque()
    dist = [[987654321 for _ in range(M)] for _ in range(N)]
        
    dx=[-1,1,0,0]
    dy=[0,0,1,-1]
    
    # 시작점 찾아서 큐에 추가
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                q.append((i,j,0))
                dist[i][j] = 0
        if q:
            break
            
    while q:
        x,y,c = q.popleft()
        
        if board[x][y] == 'G':
            return c
        
        for i in range(4):
            nx = x
            ny = y
            
            # 해당 방향으로 미끄러지며 이동 가능한 위치 찾기
            while 0<=nx+dx[i]<N and 0<=ny+dy[i]<M and board[nx+dx[i]][ny+dy[i]] != 'D':
                nx += dx[i]
                ny += dy[i]
            
            # 이전에 해당 위치에 도달한 적이 없거나, 이전에 도달한 경우보다 적은 이동 횟수로 도달 가능한 경우
            if dist[nx][ny] > c+1:
                dist[nx][ny] = c+1
                q.append((nx,ny,c+1))
    
    # 목표 지점에 도착할 수 없는 경우
    return -1
