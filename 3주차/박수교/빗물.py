h,w = map(int, input().split())

block = list(map(int, input().split()))

res = 0

for i in range(1, w - 1):
    left_block = max(block[:i])
    right_block = max(block[i+1:])

    compare = min(left_block, right_block)

    if block[i] < compare:
        res += compare - block[i]

print(res)
