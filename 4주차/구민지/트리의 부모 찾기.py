import sys
sys.setrecursionlimit(100000)

n=int(input())
graph=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

visited=[False]*(n+1)
root=[0]*(n+1)
def dfs(x):
    if visited[x]:
        return
    visited[x]=True
    for i in graph[x]:
        if not visited[i]:  
            root[i]=x
            dfs(i)

dfs(1)
for r in root[2:]:
    print(r)
