import sys

n=int(input())
arr=list(map(int,sys.stdin.readline().strip().split()))
#arr=list(map(int,input().split()))
arr=arr[:n]
m=arr[-1]
dp=[[0]*21 for _ in range(n-1)]
dp[0][arr[0]]=1

for i in range(1,n-1):
    for j in range(21):
        if dp[i-1][j]!=0:
            n1=j+arr[i]
            n2=j-arr[i]
            
            if 0<=n1<=20:
                dp[i][n1]+=dp[i-1][j]
            if 0<=n2<=20:
                dp[i][n2]+=dp[i-1][j]

        

print(dp[-1][m])
