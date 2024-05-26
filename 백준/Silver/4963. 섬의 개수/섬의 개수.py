import sys
sys.setrecursionlimit(10**9)
from collections import deque

inputf = sys.stdin.readline

while 1:
    w,h = map(int,inputf().split())
    if w==0 and h==0:
        break
    graph = []
    visited = [[0 for _ in range(w)] for _ in range(h)]
    ans = 0
    dx= [0,0,1,-1,-1,1,-1,1]
    dy= [1,-1,0,0,-1,-1,1,1]

    def dfs(x,y):
        visited[y][x] = 1
        for i in range(8):
            mx = x+dx[i]
            my = y+dy[i]
            if 0<=mx<w and 0<=my<h:
                if not visited[my][mx]:
                    if graph[my][mx] == 1:
                        dfs(mx,my)

    for _ in range(h):
        graph.append(list(map(int,inputf().split())))
    for y in range(h):
        for x in range(w):
            if not visited[y][x] and graph[y][x] == 1:
                visited[y][x] = 1
                ans+=1
                dfs(x,y)
    print(ans)