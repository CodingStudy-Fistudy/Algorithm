from itertools import *

n ,m = map(int, input().split())
min_n = 1000000000
res = 0

board = [list(map(int, input().split())) for _ in range(n)]
loc = []

#'2'의 좌표값 loc에 저장
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            loc.append((i, j))

#조합을 사용해서 m개의 '2' 좌표위치 리스트 생성
combination = list(combinations(loc, m))

#생존한 m개의 '2' 좌표위치
for comb in combination:
  res = 0

  for i in range(n):
    for j in range(n):
      min_dis = 100000

      #1에서 생존한 m개의 '2' 좌표까지의 치킨거리를 계산해서 최소의 값을 치킨 거리로 가져옴.
      if board[i][j] == 1:
        for x, y in comb:
          dis = 0
          dis += abs(i-x)+abs(j-y)
          min_dis = min(min_dis, dis)
        res += min_dis
        
  #나올 수 있는 조합 중 치킨거리가 최소인 것을 min_n에 저장 
  min_n = min(min_n, res)


print(min_n)
