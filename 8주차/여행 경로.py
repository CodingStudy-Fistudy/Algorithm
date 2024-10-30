def solution(tickets):
    
    answer = ["ICN"] 
    visited = [False] * len(tickets)
    
    def dfs(airport, path): 
        if len(path) == len(tickets) + 1:
            answer.append(path)
            return
        
        for idx, ticket in enumerate(tickets):
            if ticket[0] == airport and not visited[idx]:
                visited[idx] = True
                dfs(ticket[1], path + [ticket[1]]) 
                # 만약 가능한 경로가 두 개일 경우 고려 -> 이 부분 처리를 못해서 테케1 통과를 못한 것 같음.
                visited[idx] = False 
                
    dfs("ICN", ["ICN"])
    
    del answer[0]
    
    answer.sort()

    return answer[0]

#=====================================
#dfs풀이 -> TEST CASE 1번 런타임 에러 오류 -> hubo에 아무것도 들어가지 않아 hubo[0] 접근할 때 인덱스 에러 발생한듯
def solution(tickets):
    global hubo
    hubo = []
    ICN = []
    
    for i in tickets:
        if i[0] == "ICN":
            ICN.append(i)
            
            
    def dfs(s, e, route, cnt, t):
        global hubo
        route.append(e)
        if cnt == len(tickets)-1:
            hubo.append(route)
            return 
        for tic in range(len(tickets)):
            if e == tickets[tic][0] and t[tic] == 0:
                if tic == 0:
                    print(s,e,tickets[tic])
                t[tic] = 1
                dfs(tickets[tic][0], tickets[tic][1], route, cnt + 1, t)
                
        return route
            
    #인천공항 출발 
    for i in ICN:
        route = []
        t = [0] * len(tickets)      
        route.append(i[0])
        t[tickets.index(i)] = 1
        a = dfs(i[0], i[1], route, 0, t)
        
    hubo.sort()
    return hubo[0]
