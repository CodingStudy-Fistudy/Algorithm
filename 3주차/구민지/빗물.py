import sys 
row,col=map(int,input().split())
h=list(map(int,sys.stdin.readline().strip().split()))
ans=0
for i in range(1,col-1):
    l=max(h[:i])
    r=max(h[i+1:])
    if l>h[i] and r>h[i]:
        ans+=min(l,r)-h[i]
print(ans)
