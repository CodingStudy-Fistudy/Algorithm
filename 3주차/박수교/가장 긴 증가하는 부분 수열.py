#bottom up 방식 풀이

n = int(input())

tmp = list(map(int, input().split()))

dp = [0] * n

for i in range(n):
    for j in range(i+1, n):
        if tmp[i] < tmp[j] and dp[j] < dp[i] + 1:
            dp[j] = dp[j] + 1

print(max(dp) + 1)
