#두번째 풀이 -> dp
#dp를 짜는 방법을 다각도로 생각해봐야함 dp 테이블을 계산값을 저장할수도 있지만 계산값의 범위를 dp 테이블로 둘 수도 있음.
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
# dp[0][0] ~ dp[n-1][20] 
dp = [ [0]*21 for _ in range(n-1) ] 
dp[0][nums[0]] = 1

for i in range(1, n - 1):
  for j in range(21):
    #dp[i-1][j]가 0이 아닐때
    if dp[i-1][j]:
      if -1 <  j + nums[i] < 21:
        dp[i][j + nums[i]] += dp[i-1][j]
      if -1 <  j - nums[i] < 21:
        dp[i][j - nums[i]] += dp[i-1][j]
      
print(dp[-2][nums[-1]])

#첫번째 풀이 -> dfs 시간초과
def dfs(idx, num, target):
    global res
    
    if num < 0 or num > 20:
        return

    if idx == len(nums):
        if num == target:
            res += 1
            return
        else:
            return
    dfs(idx+1, num + nums[idx], target)
    dfs(idx+1, num - nums[idx], target)


n = int(input())
nums = list(map(int, input().split()))

res = 0
tg = nums[-1]
nums = nums[:-1]

dfs(1, nums[0], tg)
print(res)
