import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def dijkstra(n, maps, start):
    queue = deque([[start, 0]])
    dist = [1e9 for i in range(n+1)]
    dist[start] = 0
    while queue:
        q, cnt = queue.popleft()
        # 현재 큐가 이미 갱신되었다면 CONTINUE
        if dist[q] < cnt:
            continue
        # 현재 노드와 연결된 노드 탐색
        for next_node in maps[q]:
            # 현재 카운트보다 + 1 이라면? 다음노드 값 갱신
            if dist[next_node] > cnt + 1:
                dist[next_node] = cnt + 1
                queue.append([next_node, cnt+1]) # 다음노드, 카운트 append
    return dist

def solution(n, roads, sources, destination):
    answer = []

    # 경로에 따른 맵 만들기
    maps = [[] for _ in range(n+1)]
    
    for r in roads:
        maps[r[0]].append(r[1])
        maps[r[1]].append(r[0])

    dist = dijkstra(n, maps,destination)
    
    for i in sources:
        if dist[i] == 1e9:
            answer.append(-1)
        else:
            answer.append(dist[i])
    return answer
