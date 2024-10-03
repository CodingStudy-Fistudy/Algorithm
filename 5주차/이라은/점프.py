n = int(input())

l = []
for _ in range(n):
    l.append(list(map(int, input().split())))

dp = [[0]*n for _ in range(n)]
dp[0][0] = 1 # 시작 범위는 1로 둔다

for i in range(n):
    for j in range(n):
        if i == n-1 and j==n-1: # 범위를 넘어가면 제외 
            continue
        nxt = l[i][j]
        if 0 <= i + nxt < n: # 우측 범위 안넘으면 다음 갈수있는 방향에 현재 방향 더해주기
            dp[i+nxt][j] += dp[i][j]
        if 0 <= j + nxt < n: # 아래쪽도 똑같이 해준다
            dp[i][j+nxt] += dp[i][j]
            
# 도착점에 몇개나 오는지 출력
print(dp[n-1][n-1])
