import heapq

def solution(n, edge):
    answer = 0
    graph=[[] for _ in range(n+1)]
    for e in edge:
        a,b=e
        graph[a].append([b,1])
        graph[b].append([a,1])
        
    INF=int(1e9)
    distance=[INF]*(n+1)
    max_dist=0
    def dijkstra(x):
        distance[x]=0
        q=[[0,x]]
        heapq.heapify(q)
        while q:
            dist,node=heapq.heappop(q)
            
            for i in graph[node]:
                cost=dist+i[1]
                if cost<distance[i[0]]:
                    distance[i[0]]=cost
                    heapq.heappush(q,[cost,i[0]])
    dijkstra(1)
    answer=distance.count(max(distance[1:]))
        
    return answer
