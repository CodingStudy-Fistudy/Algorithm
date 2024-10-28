#bfs로 풀이 

from collections import deque
def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    dp = [0] * (n+1)
    
    for i,j in edge:
        graph[i].append(j)
        graph[j].append(i)     
    
    q = deque()
    q.append(1)
    
    while q:
        k = q.popleft()
        
        for i in graph[k]:
            if dp[i] == 0:
                dp[i] = dp[k] + 1
                q.append(i)
            else:
                dp[i] = min(dp[i], dp[k]+1)
                
    dp[1] = 0
    max_n = max(dp)
    
    return dp.count(max_n)
