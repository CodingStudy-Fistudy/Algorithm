from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for i in range(n+1)]
    for e in edge:
        a, b = e[0], e[1]
        graph[a].append(b)
        graph[b].append(a)    

    dist = [0] * (n+1) # 1로부터의 거리를 담는 배열
    q = deque() 
    q.append(1)
    dist[1] = 1 # 1에서 1은 1

    while q:
        x = q.popleft()
        for node in graph[x]:
            if dist[node] == 0:
                q.append(node)
                dist[node] = dist[x] + 1
    
    max_dist = max(dist)
    for j in dist:
        if j == max_dist:
            answer += 1
    return answer
