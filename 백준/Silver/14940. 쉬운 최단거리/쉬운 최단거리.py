import sys
inputf = sys.stdin.readline
N,M = map(int,inputf().split())
matrix = []
mx,my = 0,0
for _ in range(N):
    matrix.append(list(map(int,inputf().split())))
for i in range(N):
    if 2 in matrix[i]:
        my=i
        mx=matrix[i].index(2)
visited=[[0 for _ in range(M)] for _ in range(N)]
answer =[[0 for _ in range(M)] for _ in range(N)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
queue = [(mx,my)]
while queue:
    x, y = queue.pop(0)
    visited[y][x] = 1
    for i in range(4):
        X = x+dx[i]
        Y = y+dy[i]
        if 0<=X<M and 0<=Y<N:
            if matrix[Y][X]==1 and visited[Y][X]==0:
                queue.append((X,Y))
                visited[Y][X] = 1
                answer[Y][X] = answer[y][x]+1
for i in range(N):
    for j in range(M):
        if visited[i][j]==0 and matrix[i][j]!=0:
            answer[i][j]=-1
for i in range(N):
    print(*answer[i])