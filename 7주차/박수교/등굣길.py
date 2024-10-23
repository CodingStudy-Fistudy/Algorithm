#두번째 풀이 -> dp로 각 자리까지 올 수 있는 경우의수를 갱신해서 가져옴

def solution(m, n, puddles):
    dp = [[0 for _ in range(m)] for _ in range(n)]
    
    for x,y in puddles:
        dp[y-1][x-1] = -1
        
    for i in range(m):
        if dp[0][i] != -1:
            dp[0][i] = 1
        else:
            break
    for j in range(n):
        if dp[j][0] != -1:
            dp[j][0] = 1
        else:
            break
            
    for i in range(1,n):
        for j in range(1,m):
            if dp[i][j] == -1:
                continue
            
            #위에서만 온 경우
            if dp[i][j] >= 0 and dp[i][j-1] < 0:
                dp[i][j] = dp[i-1][j]
                
            #왼쪽에서만 온경우
            elif dp[i][j] >= 0 and dp[i-1][j] < 0:
                dp[i][j] = dp[i][j-1]
                
            #둘 다에서 온경우
            elif dp[i][j] >= 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
    return dp[n-1][m-1] % 1000000007

# =======================================================================================
# 첫번째 풀이 - dfs로 풀이했더니 테스트케이스 8번에서 시간초과남
answer = 0
def solution(m, n, puddles):
    board = [['1' for _ in range(m)] for _ in range(n)]
    
    for x,y in puddles:
        board[y-1][x-1] = '0'
        
    def dfs(x,y):
        global answer
        
        if x == n-1 and y == m-1:
            answer += 1
            return
        
        if x < 0 or x > n-1 or y < 0 or y > m-1:
            return
        
        if board[x][y] == '0':
            return
        
        dfs(x+1, y)
        dfs(x, y+1)    
        return
    
    dfs(0,0)
    return answer
