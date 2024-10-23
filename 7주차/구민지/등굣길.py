def solution(m, n, puddles):
    distance=[[0]*m for _ in range(n)]
    for p in puddles:
        a,b=p
        distance[b-1][a-1]=-1
    distance[0][0]=1
    
    for r in range(n):
        for c in range(m):
            if distance[r][c]==-1:
                continue
            if 0<=r-1<n and distance[r-1][c]>0:
                distance[r][c]+=distance[r-1][c]
            if 0<=c-1<m and distance[r][c-1]>0:
                distance[r][c]+=distance[r][c-1]
        
    return distance[-1][-1]%1000000007
