from collections import deque

# m 가로, n 세로
m, n = map(int,input().split())

# 토마토 밭
l = []
for _ in range(n):
    row = list(map(int, input().split()))
    l.append(row)

# 상 하 좌 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 안익은게 하나라도 있으면 True
all_tomato = False
for i in range(n):
    for j in range(m):
        if l[i][j] == 0:
            all_tomato = True 

# bfs 탐색으로 토마도 익히기
def bfs():
    while q:
        y, x = q.popleft() # 세로, 가로
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= ny < n and 0 <= nx < m and l[ny][nx] == 0:
                l[ny][nx] = l[y][x] + 1
                q.append((ny, nx))

if all_tomato == False: 
    days = 0
    
else:                                    
    q = deque()
    for i in range(n):
        for j in range(m):
            if l[i][j] == 1:
                q.append((i,j))
            
    bfs() # 시작

    flag = False # 안익은게 있는지 판단
    days = 0
    
    for i in range(n):
        for j in range(m):
            if l[i][j] == 0:
                flag = True

    if flag == True: # 안익었으면 음수출력
        days = -1
    else:
        for i in range(n):
            for j in range(m):
                days = max(days, l[i][j])
        days -= 1
                
print(days)
