from collections import deque
import sys 

s=list(str(sys.stdin.readline().strip()))
s_dq=deque(s)
str_arr=[]
stack=[]
while s_dq:
    curr_s=s_dq.popleft()
    if curr_s==" ":
        str_arr.append(''.join(stack))
        str_arr.append(" ")
        stack=[] 
    elif curr_s=='<':
        if stack:
            str_arr.append(''.join(stack))
            stack=[]
        stack.append(curr_s)
        while curr_s!='>':
            curr_s=s_dq.popleft()
            stack.append(curr_s)
        str_arr.append(''.join(stack))
        stack=[]
    else:
        stack.append(curr_s)
        
if stack:
    str_arr.append(''.join(stack))

for i in str_arr:
  if i[0]=='<':
    print(i,end='')
  else:
    print(i[::-1],end='')
