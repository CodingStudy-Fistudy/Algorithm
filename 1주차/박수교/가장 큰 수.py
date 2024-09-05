#문자열 비교 연산의 경우 첫번째 인덱스부터 비교 및 정렬 연산을 수행. 같으면 그 다음 인덱스 비교 수행
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x : x * 3, reverse = True)
    return str(int(''.join(numbers)))

#=====================================================================================================
#시행 착오 풀이들 .. 

#시도 1)
# 전체 나올 수 있는 수 조합 뽑고 max로 return 했더니 시간초과 뜸.
# from itertools import permutations

# numbers = list(map(str, numbers))
# numbers = list(permutations(numbers, len(numbers)))
# return max(list(map(lambda x : ''.join(x), numbers)))

#시도 2)
# 맨 처음에 있는 자릿수 별로(9,5,3) 숫자를 나눠 정렬을 수행 후 붙이는 방식
# 이렇게 풀게 될 경우, 붙어있는 애들끼리의 조합으로만 큰 수를 만들 수 있는 한계로 1~6까지 테스트 케이스 오류가 발생함.
# def solution(numbers):
#     numbers = list(map(str, numbers))
#     n = sorted(list(set(map(lambda x : x[0], numbers))), reverse = True)
#     answer = ''
    
#     if n == ['0']:
#         return "0"
    
#     for i in n:
#         tmp = []
#         res = ''
#         #첫 숫자가 같은 애들끼리 묶음
#         for j in numbers:
#             if j[0] == i:
#                 tmp.append(j)
#         #1개면 바로 answer에 붙이기
#         if len(tmp) == 1:
#             res += tmp[0]
#             answer += res
#         #2개면 비교해서 더 큰 수를 answer에 붙이기
#         elif len(tmp) == 2:
#             res += max(tmp[0]+tmp[1], tmp[1]+tmp[0])
#             answer += res
#         #3개 이상이면 res와 비교하면서 큰 수 갱신해서 answer에 붙이기
#         else:
#             res = max(tmp[0]+tmp[1], tmp[1]+tmp[0])
#             for k in range (2,len(tmp)):
#                 res = max(res+tmp[k], tmp[k]+res)
#             answer += res
            
#     return answer
