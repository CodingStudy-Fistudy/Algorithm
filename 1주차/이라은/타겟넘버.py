def solution(numbers, target):
    answer = 0
    
    def dfs(count, start):
        nonlocal answer
        
        if count == len(numbers):         
            
            if start == target:
                answer += 1
            else:
                return
        
        else:
            dfs(count+1, start + numbers[count])
            dfs(count+1, start - numbers[count])

    dfs(0, 0)
    
    return answer
