from collections import deque

def solution(s):
    stack=[]
    q=deque(s)
    while q:
        p=q.popleft()
        if len(stack)==0:
            stack.append(p)
            continue
        else:
            if stack[-1]=="(" and p==")":
                stack.pop()
            else:
                stack.append(p)
                
    if stack:
        return False
    return True
