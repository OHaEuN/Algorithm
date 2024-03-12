import sys
inputf = sys.stdin.readline
from collections import deque

M,N = map(int,inputf().split())
box = []
for _ in range(N):
    box.append(list(map(int,inputf().split())))
dx = [1,-1,0,0]
dy = [0,0,1,-1]
q = deque([])
answer = 0

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            q.append((j,i))

def bfs():
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<M and 0<=ny<N:
                if box[ny][nx] == 0:
                    box[ny][nx] = box[y][x] +1
                    q.append((nx,ny))

bfs()
for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            print(-1)
            exit(0)
    answer = max(max(box[i]),answer)

print(answer-1)