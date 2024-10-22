# 6 -> 3 * 3 s//n
# 27 -> 9 * 9* 9 s//n


def solution(n, s):
    answer = []
    
    if n > s:
        answer = [-1]
        
    else:
        for _ in range(n):
            answer.append(s//n)
            
        for i in range(s%n):
            answer[i] += 1 
        answer.sort()
        
    return answer
