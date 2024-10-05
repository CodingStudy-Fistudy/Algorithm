#14999번 백준 연산자 끼워넣기
#백트래킹은 주로 dfs로 구현한다고 함

n = int(input())

num_list = list(map(int, input().split()))

# + - * /
pl, mi, mul, div = map(int, input().split())

def dfs(N, pl, mi, mul, div, num):
    global max_v, min_v
    if n == N:
        max_v = max(num, max_v)
        min_v = min(num, min_v)
        return

    if pl > 0:
        dfs(N+1, pl-1, mi, mul, div, num + num_list[N])
    if mi > 0:
        dfs(N+1, pl, mi-1, mul, div, num - num_list[N])
    if mul > 0:
        dfs(N+1, pl, mi, mul-1, div, num * num_list[N])
    if div > 0:
        if num < 0:
            dfs(N + 1, pl, mi, mul, div - 1, -(-num // num_list[N]))
        else:
            dfs(N + 1, pl, mi, mul, div - 1, num // num_list[N])

max_v = -1e10
min_v = 1e10
dfs(1, pl, mi, mul, div, num_list[0])
print(max_v)
print(min_v)
