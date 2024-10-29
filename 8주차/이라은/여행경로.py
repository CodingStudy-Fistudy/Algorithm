from collections import deque
def solution(tickets):
    answer = []
    q = deque()
    q.append(("ICN",["ICN"], []))
    
    while q:
        airport, path, used = q.popleft()
        # 티켓을 모두 썼을때만 answer append
        if len(used) == len(tickets):
            answer.append(path)
        
        for idx, ticket in enumerate(tickets):
            if ticket[0] == airport and not idx in used:
                q.append((ticket[1], path+[ticket[1]], used+[idx]))
                
    
    answer.sort()

    return answer[0]

# from collections import deque

# def solution(tickets):
#     answer = [] 
#     q = deque()
#     start = []
#     visited = [False] * len(tickets) 
    
#     # 시작점 찾기
#     for i in range(len(tickets)):
#         if tickets[i][0] == "ICN":
#             start.append((tickets[i], i))
#     start.sort()
#     q.append((start[0]))
    
#     answer.append(start[0][0][0])

#     while q:
#         now = q.popleft()
#         # print(now)
#         visited[now[1]] = True
#         answer.append(now[0][1])
#         tmp = []
#         for i in range(len(tickets)):
#             if now[0][1] == tickets[i][0] and not visited[i]:
#                 tmp.append((tickets[i], i))
#         if tmp:
#             tmp.sort()
#             q.append(tmp[0])
            
#     return answer
