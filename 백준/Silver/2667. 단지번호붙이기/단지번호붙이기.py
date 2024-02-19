import sys
inputf = sys.stdin.readline
from collections import deque

N = int(inputf())
ans = []
mp = []
for _ in range(N):
    mp.append(list(map(int,inputf().strip())))
visited = [[0 for _ in range(N)] for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    cnt = 0
    q = deque([(x,y)])
    visited[y][x] = 1
    while q:
        cnt += 1
        X,Y = q.popleft()
        for i in range(4):
            mx = X+dx[i]
            my = Y+dy[i]
            if 0<=mx<N and 0<=my<N:
                if not visited[my][mx]:
                    visited[my][mx] = 1
                    if mp[my][mx] == 1:
                        q.append((mx,my))
                        
    ans.append(cnt)

for x in range(N):
    for y in range(N):
        if not visited[y][x]:
            if mp[y][x] == 1:
                bfs(x,y)

print(len(ans))
ans.sort()
for a in ans:
    print(a)