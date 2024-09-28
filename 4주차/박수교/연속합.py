#1912 백준 연속합

n = int(input())

tmp = list(map(int, input().split()))

plus = 0

dp = [0] * n
dp[0] = tmp[0]

for i in range(1, n):
    dp[i] = max(tmp[i], dp[i-1] + tmp[i])
    
print(max(dp))

#=================================================
#처음 코드 -> 답은 맞게 나오나 시간 초과됨 / 시간복잡도 O(n^2)
#1912 백준 연속합

# n = int(input())

# tmp = list(map(int, input().split()))

# plus = 0

# dp = [0] * n

# for i in range(n):
#     dp[i] = tmp[i]
#     plus = tmp[i]
#     for j in range(i+1, n):
#         plus += tmp[j]
#         dp[i] = max(dp[i], plus) 
        
        

# print(max(dp))
