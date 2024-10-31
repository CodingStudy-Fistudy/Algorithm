n,d,k,c=map(int,input().split())
sushi_arr=[] 
for i in range(n):
    s=int(input())
    sushi_arr.append(s)

max_len=0
sushi_arr+=sushi_arr[:k]
for i in range(n):
    tmp=set(sushi_arr[i:i+k])
    if c not in tmp:
        curr_l=len(tmp)+1
    else:
        curr_l=len(tmp)
    if curr_l>max_len:
        max_len=curr_l
print(max_len)
