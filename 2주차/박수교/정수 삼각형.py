def solution(triangle):
    #dp 테이블 구성
    dp = [[0] * i for i in range(1, len(triangle) + 1)]

    #초기값 설정
    dp[0][0] = triangle[0][0]
    dp[1][0] = triangle[1][0] + triangle[0][0]
    dp[1][1] = triangle[1][1]+ triangle[0][0]

    for i in range(2, len(triangle)):
        for j in range(len(triangle[i])):
            #인덱스 0번값 처리
            if j == 0:
                dp[i][j] = triangle[i][j] + dp[i-1][j]
                continue
            #인덱스 len(triangle[i])-1번 값 처리
            elif j == len(triangle[i])-1:
                dp[i][j] = triangle[i][j] + dp[i-1][j-1]
                continue
            #그 외 나머지 값들 처리
            dp[i][j] = triangle[i][j] + max(dp[i-1][j], dp[i-1][j-1])
    
    #마지막줄에서 가장 큰 값 return         
    return max(dp[len(triangle)-1])
