from itertools import *

def solution(numbers):
    answer = 0
    flag = 0
    
    #가능한 수 조합 뽑아서 중복 제거하고 int로 변환
    nums = []
    for i in range(1, len(numbers) + 1):
        nums.append(list(set(map(''.join, permutations(numbers, i)))))
    nums = list(set(map(int, sum(nums, []))))
    
    #소수 판별
    for i in nums:
        #0, 1 제외
        if i < 2:
            continue
            
        for j in range(2,i):
            if i % j == 0:
                flag = 1
                break
        #1, 자신을 제외한 약수 존재함으로 continue
        if flag == 1:
            flag = 0
            continue
            
        #위에 조건에 다 안걸려서 소수 판별    
        answer += 1
    
    return answer
