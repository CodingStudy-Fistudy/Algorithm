import math
def solution(brown, yellow):
    if math.sqrt(yellow) == int(math.sqrt(yellow)):
        return [math.sqrt(yellow)+2, math.sqrt(yellow)+2]
    
    #가로+세로 값
    n = (brown - 4) // 2
    
    for i in range(1,n+1):
        if (i * (n-i)) == yellow:
            return [i+2, (n-i)+2] if i > n-i else [(n-i)+2, i+2]
