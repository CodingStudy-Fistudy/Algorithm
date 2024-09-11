from collections import deque
from itertools import permutations

def calculate(a,b,op):
    if op=='+':
        return a+b
    elif op=='-':
        return a-b 
    else:
        return a*b

def change_to_dq(expression):
    dq=deque([])
    n=""
    for e in expression:
        if e.isdigit():
            n+=e
        else:
            dq.append(int(n))
            n=""
            dq.append(e)
    dq.append(int(n))
    return dq

def solution(expression):
    dq=change_to_dq(expression)
    max_res=0
    oper_permutation=permutations(['+','-','*'])
    for oper in oper_permutation:
        q=dq.copy()
        stack=[]
        for op in oper:
            while q:
                n=q.popleft()
                if str(n).isdigit():
                    stack.append(n)
                else:
                    if n==op:
                        num=calculate(stack.pop(),q.popleft(),op)
                        stack.append(num)
                    else:
                        stack.append(n)
            if len(stack)==1:
                res=abs(stack[0])
                if res>max_res:
                    max_res=res
            q=deque(stack)
            stack=[]
    return max_res
    
