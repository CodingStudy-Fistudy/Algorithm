from itertools import combinations
import sys

n,m=map(int,input().split())
homes=[]
chickens=[]
chicken_cnt=0
for i in range(n):
    tmp=list(map(int,sys.stdin.readline().strip().split()))
    for j in range(n):
        if tmp[j]==1:
            homes.append([i,j])
        elif tmp[j]==2:
            chickens.append([i,j])
            chicken_cnt+=1

distance=[]
for hx,hy in homes:
    d=[]
    for cx,cy in chickens:
        dist=abs(hx-cx)+abs(hy-cy)
        d.append(dist)
    distance.append(d)

idx_comb=list(combinations([n for n in range(0,chicken_cnt)],m))
# print(idx_comb)
INF=int(1e9)
min_ans=int(1e9)
for idx in idx_comb:
    curr_sum=0
    min_num=INF
    for d in distance:
        tmp=[]
        for i in idx:
            tmp.append(d[i])
        curr_sum+=min(tmp)
    if curr_sum<min_ans:
        min_ans=curr_sum

print(min_ans)
