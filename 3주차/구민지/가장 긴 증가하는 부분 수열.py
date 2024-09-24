import sys

n=int(input())
arr=list(map(int,sys.stdin.readline().strip().split()))
d=[1]*n
for i in range(1,n):
    max_len=1
    for j in range(i-1,-1,-1):
        if arr[j]<arr[i]:
            if max_len<d[j]+1:
                max_len=d[j]+1
    d[i]=max_len
    
print(max(d))
