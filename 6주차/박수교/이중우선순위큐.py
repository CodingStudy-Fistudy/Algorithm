#힙을 사용할 때 최대힙으로 변형하는 방법은 여러가지가 있음
#안에 값들을 다 -로 갱신해서 heappop을 수행해서 부호만 바꿔주면 최대로 바뀜
#또는 튜플로 우선순위를 같이 구성하면 (-n, n) heap은 자동으로 0번째 인덱스를 기준으로 heap정렬을 수행하기 때문에 heappop(heap)[1]을 찾으면 자동으로 큰값이 나옴 => -와 +가 혼용된 경우는 사용하기 어려움 ..

#nlargest, nsmallest 라는 함수가 있는데 힙에서 가장 큰 수 n개 이런식으로 뽑아오는 함수
#heapq.nlargest(뽑을수, heap)[0] 하면 최대값을 뽑을 수 있음 (뽑을 수 -> 1로 설정)
heap은 기본적으로 리스트로 구성되어있어서 pop연산으로 최대 최소 뽑는 연산을 같이 수행할 수 있음.


import heapq
def solution(operations):
    heap = []
    for i in operations:
        if i.startswith("I"):
            heapq.heappush(heap, int(i.split()[1]))
        elif i == "D -1":
            if heap == []:
                continue
            heapq.heappop(heap)
        elif i == "D 1":
            if heap == []:
                continue
            heap.pop(heap.index(heapq.nlargest(1, heap)[0]))
            
    if heap == []:
        return [0,0]
    return heapq.nlargest(1, heap)[0], heapq.nsmallest(1, heap)[0]


    
