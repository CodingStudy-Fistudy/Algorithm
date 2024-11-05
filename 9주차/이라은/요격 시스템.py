def solution(targets):
    answer = 0
    
    targets.sort(key = lambda x : [x[1], x[0]])
    
    s = e = 0
    
    for target in targets:
        if target[0] >= e: # 직전의 끝나는 지점보다 같거나 크다면 (같은 경우에도 못막음)
            answer += 1 
            e = target[1]
            
    return answer
