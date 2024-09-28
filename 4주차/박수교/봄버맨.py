#16918번 백준 봄버맨
from collections import deque

r, c, n = map(int, input().split())

board = []
bomb = deque()

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

#board 기본세팅
for i in range(r):
    row = list(input())
    board.append(row)

    for j in range(c):

        if row[j] == "O":
            bomb.append([i, j])

def bfs(board, bomb, t):
    while t < n:

        for i in range(r): 
            for j in range(c):
                if board[i][j] == '.':
                    board[i][j] = 'O'


        t += 1
        if t == n:
            return 

        while bomb: 
            x, y = bomb.popleft()
            board[x][y] = '.'
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if -1 < nx < r and -1 < ny < c:
                    board[nx][ny] = '.'

        for i in range(r):
            for j in range(c):
                if board[i][j] == 'O':
                    bomb.append([i, j])
        t += 1
        if t == n:
            return 

    
bfs(board, bomb, 1)


for row in board:
    print(''.join(row))





