from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
arr =[]
maxNum = 0
for i in range(n):
    arr.append(list(map(int,input().split())))
    for j in range(n):
        if arr[i][j] > maxNum:
            maxNum = arr[i][j] 


dx = [0 ,0, 1, -1]
dy = [1, -1, 0 ,0]
def bfs(a, b, value, visited):
    q = deque()
    q.append((a, b))
    visited[a][b] = 1
 
    while q:
        x, y = q.popleft()
 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] > value and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))

answer = 0
for i in range(maxNum):
    visited= [[0]*n for _ in range(n)]
    count = 0

    for x in range(n):
        for y in range(n):
            if arr[x][y] > i and visited[x][y] == 0:
                bfs(x,y,i,visited)
                count=count+1
    
    if answer < count :
        answer = count

print(answer)