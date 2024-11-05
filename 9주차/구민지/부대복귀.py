import heapq
    
def solution(n, roads, sources, destination):
    answer = []
    graph=[[] for _ in range(n+1)]
    for road in roads:
        r1,r2=road
        graph[r1].append([r2,1])
        graph[r2].append([r1,1])
        
    INF=int(1e9)
    distance=[INF]*(n+1)
    def dijkstra(x):
        distance[x]=0
        q=[[0,x]]
        heapq.heapify(q)
        while q:
            d,n=heapq.heappop(q)
            for node in graph[n]:
                cost=d+node[1]
                if cost<distance[node[0]]:
                    distance[node[0]]=cost
                    heapq.heappush(q,[cost,node[0]])
        return distance
    
    dijkstra(destination)
    for s in sources:
        if distance[s]==INF:
            answer.append(-1)
        else:
            answer.append(distance[s])
        
    return answer
