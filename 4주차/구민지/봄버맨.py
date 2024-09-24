import sys 

row,col,n=map(int,input().split())
graph=[]
for _ in range(row):
    tmp=list(sys.stdin.readline().strip())
    tmp_list=[]
    for t in tmp:
        if t=='O':
            tmp_list.append(0)
        else:
            tmp_list.append(-1)
    graph.append(tmp_list)

def set_bomb(time,graph):
  for r in range(row):
    for c in range(col):
      if graph[r][c]==-1:
        graph[r][c]=time
  return graph

def explosion(time,graph):
  for r in range(row):
    for c in range(col):
      if graph[r][c]==time-3:
        graph[r][c]=-1
        for rm,cm in [[1,0],[-1,0],[0,1],[0,-1]]:
          if 0<=r+rm<row and 0<=c+cm<col:
            if graph[r+rm][c+cm]!=time-3:
                graph[r+rm][c+cm]=-1
  return graph

time=1
if n%2==0:
  for i in range(row):
    print("O"*col)
else:
  while time<n:
    time+=1
    if time%2==0:
        graph=set_bomb(time,graph)
        continue 
    graph=explosion(time,graph)

  for r in range(row):
    for c in range(col):
      if graph[r][c]==-1:
        print(".",end='')
      else:
        print("O",end='')
    print()

  
