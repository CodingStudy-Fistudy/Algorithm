from itertools import *
#곱이 최대가 되려면 조합을 다 뽑아봐야 체크할 수 있을것같은데
#아님 n번 for문 .. while ..?
#dp ..?

#test 케이스 보니까 왠지 중간에 있는 애들 곱한값이 제일 곱이 크게 나오는 것 같아서
#s를 n으로 나눠주고 n -= 1 하는식으로 갱신했더니 풀렸음.

def solution(n, s):
    tmp = []
    while True:
        if s // n == 0:
            return [-1]
        m = n
        tmp.append(s // n)
        n -= 1
        if n == 1:
            tmp.append(s - (s // m))
            break
        s = s - s // m
    return tmp


#===============================================================================================================

#첫번째 풀이 -> 시간초과 ^.^
#중복조합으로 뽑아온다음에 합이 s랑 같은애만 필터링했는데 중복조합 뽑아오는 과정에서 시간이 너무 오래걸린 것 같음.

from itertools import *

def solution(n, s):
    nn = list(combinations_with_replacement(list(range(1, s)), n))
    nn = list(filter(lambda x : sum(x) == s, nn))
    
    if nn == []:
        return [-1]
    nn.sort(key = lambda x:x[0]*x[1], reverse = True)
    return list(nn[0])

