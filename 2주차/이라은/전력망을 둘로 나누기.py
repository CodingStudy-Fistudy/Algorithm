from collections import deque

def solution(n, wires):
    answer = n
    q = deque()
    graph = []
    
    for _ in range(n+1):
        row = []
        graph.append(row)       
    
    # 트리 그래프 생성
    for wire in wires:
        v1, v2 = wire[0], wire[1]
        graph[v1].append(v2)
        graph[v2].append(v1)
    print(graph)
    
    def bfs(start, visited, graph):
        q = deque([start])
        cnt = 1
        visited[start] = True
        while q:
            now = q.popleft() #지금 탐색하는 지점
            for node in graph[now]:
                if not visited[node]:
                    visited[node] = True
                    q.append(node)
                    cnt += 1
        return cnt
                        
    # wire가 하나씩 없다고 가정
    for start, end in wires:
        visited = [False] * (n+1) 
        visited[end] = True # 방문처리 배열을 활용하여 매 반복마다 방문처리 한다
        result = bfs(start, visited, graph)    
        answer = min(answer, abs(result - (n-result)))
    
    return answer
