import sys
from collections import deque
input = sys.stdin.readline


M, N, H = map(int,input().split())

matrix =[[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[False]*M for _ in range(N)] for _ in range(H)]


dx= [-1,1,0,0,0,0]
dy= [0,0,-1,1,0,0]
dz= [0,0,0,0,-1,1]

queue = deque()
cnt = 0

def bfs():
    while queue:
        x,y,z = queue.popleft()

        for i in range(6): # 주변 토마토 탐색
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if nx < 0 or nx >= H or ny < 0 or ny >= N or nz < 0 or nz >= M: # 범위 값 벗어나면
                continue

            if matrix[nx][ny][nz] == 0 and visited[nx][ny][nz] == False: # 안익은 토마토면서 방문 x인 경우
                matrix[nx][ny][nz] = matrix[x][y][z] + 1 
                queue.append((nx,ny,nz)) # 새로 익은 토마토 주변 탐색해야 하니까 queue에 append
                visited[nx][ny][nz] = True

# 익은 토마토 좌표 queue에 넣은 다음 bfs 실행
for a in range(H):
    for b in range(N):
        for c in range(M):
            if matrix[a][b][c] == 1 and visited[a][b][c] == False:
                queue.append((a,b,c))
                visited[a][b][c] = True
bfs()

# 토마토 확인
for box in matrix:
    for row in box:
        for num in row:
            if num == 0:
                print(-1)
                exit(0)
        cnt = max(cnt, max(row))

print(cnt - 1)
# 모두 1인 경우 0 출력되므로 예외 처리 필요 없음
