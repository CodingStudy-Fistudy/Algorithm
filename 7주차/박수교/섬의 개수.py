def dfs(i, j):
    if 0 > i or i > h-1 or 0 > j  or j > w-1:
        return False

    if board[i][j] == 0 or board[i][j] == -1:
        return False
    
    board[i][j] = -1
    
    dfs(i-1, j)
    dfs(i+1, j)
    dfs(i, j-1)
    dfs(i, j+1)
    
    dfs(i-1, j+1)
    dfs(i+1, j+1)
    dfs(i+1, j-1)
    dfs(i-1, j-1)
    
    return True

while True:
    w, h = map(int, input().split())
    cnt = 0
    
    if w == 0 or h == 0:
        exit()
    
    board = [list(map(int, input().split())) for _ in range(h)]
    
    
    for i in range(h):
        for j in range(w):
            if board[i][j] == 1:
                dfs(i, j)
                cnt += 1
                
    print(cnt)
