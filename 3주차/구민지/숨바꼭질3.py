import heapq

s, k = map(int, input().split())

INF = int(1e9)
distance = [INF] * 100001


def dijkstra(start):
    distance[start]=0
    q = [[0, start]]
    heapq.heapify(q)
    while q:
        dist, n = heapq.heappop(q)
        if distance[n]<dist:
            continue
        if k==n:
            return

        if n*2<k+2 and distance[n*2]>dist:
            distance[n*2]=dist
            heapq.heappush(q,[dist,n*2])
        if n-1>=0 and distance[n-1]>dist+1:
            distance[n-1]=dist+1
            heapq.heappush(q,[dist+1,n-1])
        if n+1<k+2 and distance[n + 1] > dist + 1:
            distance[n + 1] = dist + 1
            heapq.heappush(q,[dist + 1, n + 1])

dijkstra(s)
print(distance[k])
