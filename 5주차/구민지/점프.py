from collections import deque
import sys

n=int(input())
graph=[]
d=[[0]*n for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().strip().split())))
d[0][0]=1
for i in range(n):
    for j in range(n):
        k=graph[i][j]
        if k==0:
            continue
        if j+k<n:
            d[i][j+k]+=d[i][j]
        if i+k<n:
            d[k+i][j]+=d[i][j]

print(d[-1][-1])
