from collections import deque

def solution(n, roads, sources, destination):
    ans = []
    visited = [-1] * (n+1)
    loc = [[] for _ in range(n+1)]
    for i in roads:
        a, b = i[0], i[1]
        loc[a].append(b)
        loc[b].append(a)

    q = deque()
    q.append(destination)
    visited[destination] += 1
    while q:
        now = q.popleft()
        for i in loc[now]:
            if visited[i] == -1:
                q.append(i)
                visited[i] = visited[now] + 1

    for i in sources:
        ans.append(visited[i])

    return ans
