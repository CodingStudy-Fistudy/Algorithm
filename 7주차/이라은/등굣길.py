def solution(m, n, puddles):
    
    grid = [[0] * (m + 1) for _ in range(n + 1)]
    grid[1][1] = 1 # 시작지점 1 
    
    for y in range(1, n + 1):
        for x in range(1, m + 1):
            
            # 웅덩이 발견하면 무시
            if [x, y] in puddles:
                continue
            
            # 그리드 기준 위, 왼 -> 합친 값이 현재 그리드의 값
            b1 = grid[y - 1][x]
            b2 = grid[y][x - 1]
           
            # 현재그리드 위의 위에가 웅덩이면? 현재그리드 위도 0
            if [x, y - 1] in puddles:
                b1 = 0
            # 현재그리드 왼의 기준 
            if [x - 1, y] in puddles:
                b2 = 0

            grid[y][x] += b1 + b2
            
    answer = grid[n][m] % 1000000007
    return answer
