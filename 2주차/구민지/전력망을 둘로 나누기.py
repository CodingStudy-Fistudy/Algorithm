from collections import deque

def bfs(x, wire):
    global visited, graph
    cnt = 0
    if visited[x]:
        return 0
    q = deque([x])
    while q:
        x = q.popleft()
        if visited[x]:
            continue
        visited[x] = True
        cnt += 1
        for i in graph[x]:
            if [x, i] == wire or [i,x]==wire:
                continue
            if not visited[i]:
                q.append(i)
    return cnt


def solution(n, wires):
    min_diff=n
    global graph, visited
    graph = [[] for _ in range(n + 1)]
    for x,y in wires:
        graph[x].append(y)
        graph[y].append(x)

    for i in range(len(wires)):
        visited = [False for _ in range(n + 1)]
        cnt = 0
        cnt_list = []
        for j in range(1, n + 1):
            cnt = bfs(j, wires[i])
            if cnt:
                cnt_list.append(cnt)

        min_diff=min(min_diff,max(cnt_list)-min(cnt_list))

    return min_diff
