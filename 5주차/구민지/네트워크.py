from collections import deque

def bfs(start):
    global graph,visited
    if visited[start]:
        return 0
    cnt=0
    q=deque([start])
    while q:
        n=q.popleft()
        if visited[n]:
            continue
        visited[n]=True
        cnt+=1
        for i in graph[n]:
            if not visited[i]:
                q.append(i)
    return cnt
        
    
def solution(n, computers):
    answer = 0
    global graph,visited
    graph=[[] for _ in range(n+1)]
    visited=[False]*n
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            if computers[i][j]:
                graph[i].append(j)

    for i in range(n):
        if bfs(i):
            answer+=1
    return answer
