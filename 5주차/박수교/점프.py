#1890번 백준 점프

board = []
n = int(input())
for _ in range(n):
    board.append(list(map(int, input().split())))

dp = [[0] * n for _ in range(n)]

dp[0][0] = 1

for i in range(n):
    for j in range(n):
        #오른쪽 끝에 도달하지 못한 경우
        if board[i][j] != 0 and dp[i][j] != 0:
            #가로로 전진
            if board[i][j] + i < n:
                dp[board[i][j] + i][j] += dp[i][j]
            #세로로 전진
            if board[i][j] + j < n:
                dp[i][board[i][j] + j] += dp[i][j]
                
print(dp[-1][-1])
