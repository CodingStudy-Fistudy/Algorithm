from itertools import permutations
from collections import deque

def solution(expression):
    max_num = 0
    
    ex = deque()
    num = ""
    
    # 숫자,기호 구분해서 deque에 추가
    for i in expression:
        if i.isdigit():
            num += i
        else:
            ex.append(num)
            ex.append(i)
            num = ""
    ex.append(num)
    
    #나올 수 있는 기호 경우의 수 생성
    operand = list(permutations(["*","-","+"], 3))

    #경우의 수만큼 계산값 구한 후 최대값 뽑기
    for oper in operand:
        ex2 = ex.copy()
        for op in oper:
            stack = []
            while ex2:
                tmp = ex2.popleft()
                if tmp == op:
                    stack.append(str(eval(stack.pop()+op+ex2.popleft())))
                else:
                    stack.append(tmp)
            ex2 = deque(stack)
        tmp_num = abs(int(ex2.pop()))
        
        if tmp_num > max_num:
            max_num = tmp_num
            
    return max_num
