import copy

def solution(rows, columns, queries):
    answer = []
    graph=[[r*columns+c for c in range(1,columns+1)] for r in range(rows)]
    new_graph=[[0]*columns for _ in range(rows)]

    INF=int(1e9)
    for query in queries:
        r1,c1,r2,c2=query
        graph2=[[0]*columns for _ in range(rows)]
        min_num=INF
        for r in range(rows):
            for c in range(columns):
                if r1-1<=r<=r2-1 and c1-1<=c<=c2-1:
                    if r1<=r<r2-1 and c1<=c<c2-1:
                        graph2[r][c]=graph[r][c]
                        continue
                    if graph[r][c]<min_num:
                        min_num=graph[r][c]
                    if c1-1<=c<c2-1 and r==r1-1:
                        graph2[r][c+1]=graph[r][c]
                    elif c==c2-1 and r1-1<=r<r2-1:
                        graph2[r+1][c]=graph[r][c]
                    elif r==r2-1 and c1-1<c<=c2-1:
                        graph2[r][c-1]=graph[r][c]
                    else:
                        graph2[r-1][c]=graph[r][c]
                    continue
                graph2[r][c]=graph[r][c]
        graph=graph2
        answer.append(min_num)

    return answer
