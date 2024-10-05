ans = 0
def solution(n, computers):
    
    global ans
    def dfs(graph,n,visited):
        global ans
        if graph[n] == []:
            visited[n] = True
            return
        
        for i in graph[n]:
            if not visited[i]:
                visited[i] = True
                dfs(graph, i, visited)

    
    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                graph[i+1].append(j+1)
        
    for k in range(1, len(graph)):
        if visited[k] == False:
            ans += 1
            dfs(graph, k, visited)
        
    return ans
