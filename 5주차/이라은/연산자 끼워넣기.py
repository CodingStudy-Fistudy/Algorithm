from itertools import permutations

n = int(input())

num = list(map(int, input().split()))

add, sub, mul, div = map(int, input().split())

# 연산자 우선순위 무시 -> 그냥 앞에서 부터 차례대로 계산
# 종료 조건 -> num 이 n 까지 왔을때 종료 (0부터 시작한다)
def dfs(idx, now, add, sub, mul, div):
    global max_num, min_num
    
    # if now < int(-1e8) or now > int(1e8):
    #     return
    
    if idx == n:
        max_num = max(max_num, now)
        min_num = min(min_num, now)
        return
    
    # 연산자가 남아 있을 때만 호출
    if add > 0:
        dfs(idx+1, now+num[idx], add-1, sub, mul, div)
    if sub > 0:
        dfs(idx+1, now-num[idx], add, sub-1, mul, div)
    if mul > 0:
        dfs(idx+1, now*num[idx], add, sub, mul-1, div)
    if div > 0:
        dfs(idx+1, int(now/num[idx]), add, sub, mul, div-1) 
        # if now < 0:
        #     dfs(idx+1, - int(-now//num[idx]), add, sub, mul, div-1)
        # else:
        #     dfs(idx+1, int(now//num[idx]), add, sub, mul, div-1)



max_num = int(-1e9) #1,000,000,000 
min_num = int(1e9) #실수말고 정수로 형변환 한다

dfs(1, num[0], add, sub, mul, div)

print(max_num)
print(min_num)
