n, d, k, c = map(int, input().split())
sushi = []
max_sushi = -1
for i in range(n):
    sushi.append(int(input()))


for i in range(n):
    if i > n-k:
        ss = sushi[i:]+sushi[:k-len(sushi[i:])]
    else:
        ss = sushi[i:i+k]

    ss = set(ss)
    if c not in ss:
        max_sushi = max(max_sushi, len(ss) + 1)
    else:
        max_sushi = max(max_sushi, len(ss))

print(max_sushi)
