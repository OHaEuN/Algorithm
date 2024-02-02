import sys
inputf = sys.stdin.readline
from collections import deque

N,M = map(int,inputf().split())
mtrx=[]
for _ in range(N):
    mtrx.append(list(inputf().strip()))
visited = [[0 for _ in range(M)] for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs():
    global answer
    q = deque()
    q.append((0,0))
    while q:
        x,y = q.popleft()
        for i in range(4):
            mx = x+dx[i]
            my = y+dy[i]
            if 0<=mx<M and 0<=my<N and mtrx[my][mx] == '1':
                if not visited[my][mx] or visited[my][mx] > visited[y][x]+1 :
                    if mx == M-1 and my == N-1:
                        print(visited[y][x]+1+1)
                        return
                    else: 
                        visited[my][mx] = visited[y][x]+1
                        q.append((mx,my))

bfs()