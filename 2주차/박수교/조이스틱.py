def solution(name):
    #알파벳 이동값 초기화
    alpha_move = 0
    #커서 이동값 초기화 -> A가 한개도 존재하지 않을 것을 고려해 초기값 설정
    cursor_move = len(name) - 1
    
    #for문을 통해 어느 인덱스를 기준으로 방향 전환을 했을때 가장 min한 값이 나오는지 조회
    for i, spell in enumerate(name):
        #알파벳 이동 횟수
        alpha_move += min(ord(spell) - 65, 91 - ord(spell))
        
        #커서 이동 횟수
        next = i+1
        while next < len(name) and name[next] == 'A':
            next += 1
            
        # 아래 3가지 경우 중 최소 이동 값으로 갱신 (i는 현재 위치 인덱스, next는 연속된 A의 마지막 인덱스)
        # 1. cursor_move = 돌아가지 않고 앞으로만 간 경우
        # 2. i*2 + (len(name) - next) = 앞으로 가다가 뒤로 다시 돌아가는 경우
        # 3. i+2 * (len(name) - next) = 뒤로 먼저 간 뒤 앞으로 다시 돌아오는 경우
        cursor_move = min([cursor_move, i * 2 + (len(name) - next), i + 2 * (len(name) - next) ])
        
    return alpha_move + cursor_move

#=====================================================================================================
#시행 착오 풀이들 .. 

#시도 1) -> 48점
#이렇게 풀이를 진행할 경우 "LABLPAJM"와 같은 반례에서 뒤로 가는게 더 최소값을 반환해서 틀린 풀이가 됨.
# def solution(name):
#     idx,res = 0,0
#     tmp = []
#     for i in range(len(name)):
#         if name[i] != 'A':
#             tmp.append(i)
#     print(tmp)
#     for i in tmp:
#         #이동거리 체크
#         if abs(idx - i) <= abs(len(name) - i + idx):
#             res += abs(idx-i)
#         else:
#             res += abs(len(name) - i + idx)
        
#         #현재위치 갱신
#         idx = i
        
#         #알파벳 체크   
#         if ord(name[i]) <= 78:
#             res += ord(name[i]) - 65
#         else:
#             res += 91 - ord(name[i])
            
#     return res

#시도 2) -> 63점
#역방향을 추가해서 "LABLPAJM"의 반례는 해결했으나, NAME의 중간에서 방향전환을 했을때 최소가 되는 케이스들 때문에 틀린 풀이가 됨. 예를 들면 "TAATAAAAAT" 이런 케이스들
#내 코드는 한 방향으로만 전진하게 짜서 문제가 안풀리는듯
# def solution(name):
#     idx,res,res2 = 0,0,1
#     tmp = []
#     for i in range(len(name)):
#         if name[i] != 'A':
#             tmp.append(i)
#     print(tmp)
    
#     #순방향으로 갔을 때 결과 체크
#     for i in tmp:
#         #이동거리 체크
#         if abs(idx - i) <= abs(len(name) - i + idx):
#             res += abs(idx-i)
#         else:
#             res += abs(len(name) - i + idx)
        
#         #현재위치 갱신
#         idx = i
        
#         #알파벳 체크   
#         if ord(name[i]) <= 78:
#             res += ord(name[i]) - 65
#         else:
#             res += 91 - ord(name[i])
    
#     #역방향 진행        
#     idx = len(name) - 1        
#     for j in range(len(tmp)-1,-1,-1):
#         #끝에서부터 시작한다는 가정하에 res2는 1에서부터 시작
#         #0번째 인덱스가 A가 아닐때 처리해주고 반복문 종료
#         if tmp[j] == 0:
#             #알파벳 체크   
#             if ord(name[tmp[j]]) <= 78:
#                 print(name[tmp[j]])
#                 res2 += ord(name[tmp[j]]) - 65
#             else:
#                 res2 += 91 - ord(name[tmp[j]])
#             break
            
        
#         if abs(idx - tmp[j]) <= abs(len(name) - idx + tmp[j]):
#             res2 += idx - tmp[j]
#         else:
#             res2 += abs(len(name) - idx + tmp[j])
            
#         idx = tmp[j]
        
#         #알파벳 체크   
#         if ord(name[tmp[j]]) <= 78:
#             print(name[tmp[j]])
#             res2 += ord(name[tmp[j]]) - 65
#         else:
#             res2 += 91 - ord(name[tmp[j]])
    
#     #순방향, 역방향 최솟값 리턴
#     return min(res,res2)
