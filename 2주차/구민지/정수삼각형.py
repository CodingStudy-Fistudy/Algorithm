def solution(triangle):
    l=len(triangle)
    distance=[[0]*l for _ in range(l)]
    distance[0][0]=triangle[0][0]
    for i in range(1,l):
        for j in range(i+1):
            if j==0:
                distance[i][j]=distance[i-1][j]+triangle[i][j]
                continue
            distance[i][j]=max(distance[i-1][j],distance[i-1][j-1])+triangle[i][j]
    return max(distance[-1])
