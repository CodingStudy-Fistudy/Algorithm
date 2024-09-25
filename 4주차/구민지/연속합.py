import sys

n=int(input())
arr=list(map(int,sys.stdin.readline().strip().split()))
d=[arr[0]]
for i in range(1,n):
    d.append(max(d[-1]+arr[i],arr[i]))
print(max(d))
  
