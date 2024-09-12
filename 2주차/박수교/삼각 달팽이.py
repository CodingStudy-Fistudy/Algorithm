def solution(n):
    #값 초기화
    top = [[0] * n for _ in range(n)]
    x,y = 0,0
    snail, dir = 1, 1
    
    for i in range(n,0,-1):
        for j in range(i):
            #step 1. 밑으로 내려가기
            if dir == 1:
                dx = x + j
                dy = y
                top[dx][dy] = snail
                snail += 1
            #step 2. 오른쪽으로 가기
            elif dir == 2:
                dy = y + j
                top[dx][y+j] = snail
                snail += 1
            #step 3. 왼쪽 대각선으로 올라가기
            elif dir == 3:
                dx -= 1
                dy -= 1
                top[dx][dy] = snail
                snail += 1
                
        #방향 전환하기
        if dir == 1:
            y += 1
            dir = 2
        elif dir == 2:
            dir = 3
        elif dir == 3:
            x = dx + 1
            y = dy
            dir = 1
    
    #2차원 1차원으로 변환
    top = sum(top, [])
    
    #0제거
    remove = [0]
    top = [i for i in top if i not in remove]
    
    return top
            
