import heapq
#값을 넣으면 자동적으로 최소 - 최대로 알아서 정렬 뺄때도 최소값이 빠짐

def solution(n, works):
    #퇴근까지 남은 시간 > 작업량 총합
    if n >= sum(works):
        return 0
    
    #부호를 반대로 해주면 최대힙 처럼 구현할 수 있음 -> 음수로 리스트 재구성
    works = [-w for w in works]
    
    #heapify => 리스트를 heap으로 변환해주는 함수
    heapq.heapify(works)
    
    print(works)
    
    for _ in range(n):
        #최대값을 하나 뺌
        i = heapq.heappop(works)
        #음수기때문에 더해주는건 사실상 값을 줄여주는것
        i += 1
        
        #값을 다시 넣음
        heapq.heappush(works, i)
    
    return sum(list(map(lambda x : x**2, works)))
