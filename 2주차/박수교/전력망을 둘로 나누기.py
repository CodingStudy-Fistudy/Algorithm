import copy
#그냥 copy 함수는 이차원 리스트에서는 먹히지 않아서 deepcopy를 사용해야함

#그래프 dfs로 순회하면서 노드 개수 구하기
def dfs(graph, now, visited, cnt):
    visited[now] = True
    cnt += 1
    for j in graph[now]:
        if not visited[j]:
            cnt = dfs(graph, j, visited, cnt)
    
    return cnt
    

def solution(n, wires):
    res = []

    #wires기반으로 graph 생성
    graph = [[] for _ in range(n+1)]
    for x,y in wires:
        graph[x].append(y)
        graph[y].append(x)

    #wires 순회하면서 한개씩 간선을 끊어서 차이의 절댓값 구하기
    for i in range(len(wires)):
        visited = [False] * (n+1)
        tmp = []
        #이차원 리스트에서 copy는 사용이 안되어 deepcopy 함수 사용
        graph_ex = copy.deepcopy(graph)
        graph_ex[wires[i][0]].remove(wires[i][1])
        graph_ex[wires[i][1]].remove(wires[i][0])

        #두개의 그래프의 노드 값을 각각 구하여 뺀 값 res에 append
        for i in range(1, n+1):
            if visited[i] == False:
                top_cnt = dfs(graph_ex, i, visited, 0)
                tmp.append(top_cnt)
        res.append(abs(tmp[0] - tmp[1]))

    #res에서 가장 min한 값 return 하기
    return min(res)
