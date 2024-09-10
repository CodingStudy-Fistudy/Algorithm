def solution(n):
    answer=[]
    triangle=[[0]*(i+1) for i in range(n)]
    moves=[[1,0],[0,1],[-1,-1]]
    k,m,r,c=0,0,-1,0
    
    for i in range(n,0,-1):
        for j in range(i):
            triangle[r][c]=k
            k+=1
            a,b=moves[m]
            r,c=r+a,c+b
        m+=1
        if m>2:
            m=0
    triangle[r][c]=k
    for t in triangle:
        answer.extend(t)
    return answer
