def solution(triangle):    
    dp = []
    for i in range(len(triangle)):
        row = []
        for j in range(len(triangle[i])):
            row.append(0)
        dp.append(row)
    dp[0][0]=triangle[0][0]
    dp[1][0]=triangle[1][0] + triangle[0][0]
    dp[1][1]=triangle[1][1] + triangle[0][0]
    
    for i in range(2, len(triangle)):
        length = len(triangle[i])
        for j in range(length):
            if j == 0:
                dp[i][0] += triangle[i][0] + dp[i-1][0]
            elif j == length-1:
                dp[i][length-1] += triangle[i][-1] + dp[i-1][-1]
            else: 
                dp[i][j] += max((triangle[i][j] + dp[i-1][j-1]), (dp[i-1][j] + triangle[i][j]))

    return max(dp[-1])
