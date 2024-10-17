a, b = map(int, input().split())
res = 1

while a != b:
    if b < a:
        res = -1
        break
    
    if str(b)[-1] == '1':
        b = int(str(b)[:-1])
    elif b % 2 == 0:
        b //= 2
    else:
        res = -1
        break
    res += 1
    
print(res)
