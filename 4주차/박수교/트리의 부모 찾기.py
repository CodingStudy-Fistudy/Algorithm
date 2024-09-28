#11725번 트리의 부모 찾기

from collections import deque

n = int(input())

tree = [[] for _ in range(n+1)]
visited = [False] * (n+1)
head = [0] * (n+1)

for _ in range(n-1):
    a,b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def bfs(tree, v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        x = queue.popleft()
        for i in tree[x]:
            if not visited[i]:
                head[i] = x
                visited[x] = True
                queue.append(i)

bfs(tree, 1, visited)

for i in range(2, n+1):
    print(head[i])
