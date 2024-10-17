from collections import deque

def solution(board):
    answer = 0
    n = len(board) #5 y 
    m = len(board[0]) #7 x
    dist = [[987654321 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        if 'R' in board[i]:
            curr_y = i
            curr_x = board[i].index('R')
            break
            
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    q = deque()
    dist[curr_y][curr_x] = 0
    q.append([curr_y, curr_x, 0])
    
    while q:
        x,y,cnt = q.popleft()
        
        if board[x][y] == 'G':
            return cnt
        
        for i in range(4):
            nx = x
            ny = y
            
            while 0<=nx+dx[i]<n and 0<=ny+dy[i]<m and board[nx+dx[i]][ny+dy[i]] != 'D':
                nx += dx[i]
                ny += dy[i]

            if dist[nx][ny] > cnt+1:
                dist[nx][ny] = cnt+1
                q.append((nx,ny,cnt+1))
                
    
    return -1
