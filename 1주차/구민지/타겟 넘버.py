cnt=0
def dfs(x,depth,numbers,target):
    global cnt
    if depth==len(numbers):
        if x==target:
            cnt+=1
        return 
    for i in [1,-1]:
        dfs(x+numbers[depth]*i,depth+1,numbers,target)
    
def solution(numbers,target):
    dfs(0,0,numbers,target)
    return cnt
    
