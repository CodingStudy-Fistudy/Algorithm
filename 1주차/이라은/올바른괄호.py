def solution(s):
    answer = True
    
    stack = []
    
    for each in s:
        if each == '(':
            stack.append('(')
        else: # ')'일 경우
            if stack and stack[-1] == '(': # 괄호 있을 경우
                stack.pop()
            else:
                stack.append(')')     
            
    print(stack)
    
    if len(stack) > 0:
        answer = False

    return answer
