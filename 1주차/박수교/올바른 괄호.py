def solution(s):
    tmp = []
    if '(' not in s or s.count('(') < s.count(')'):
        return False
    
    for i in s:
        if i == '(':
            tmp.append(i)
        elif tmp and i == ')':
            tmp.pop()
    
    return True if not tmp else False
