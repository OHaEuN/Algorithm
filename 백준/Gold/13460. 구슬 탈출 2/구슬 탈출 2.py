from collections import deque
import sys
input = sys.stdin.readline # 빠른 입출력 위한 코드
 
n, m = map(int, input().split())
mtrx = []
for i in  range(n):
    mtrx.append(list(input()))
    for j in range(m):
        if mtrx[i][j] == 'R': # 빨간구슬 위치
            rx, ry = i, j
        elif mtrx[i][j] == 'B': # 파란구슬 위치
            bx, by = i, j
 
# 상 하 좌 우로 탐색
dx = [-1, 1, 0, 0]
dy = [0, 0, -1 ,1]
 
def bfs(rx, ry, bx, by):
    q = deque()
    q.append((rx, ry, bx, by))
    visited = [] # 방문여부를 판단하기 위한 리스트
    visited.append((rx, ry, bx, by))
    count = 0
    while q:
        for _ in range(len(q)):
            rx, ry, bx, by = q.popleft()
            if count > 10: # 움직인 횟수가 10회 초과면 -1 출력
                print(-1)
                return
            if mtrx[rx][ry] == 'O': # 현재 빨간 구슬의 위치가 구멍이라면 count출력
                print(count)
                return 
            for i in range(4): 
                nrx, nry = rx, ry
                while True: # #일 때까지 혹은 구멍일 때까지 움직임
                    nrx += dx[i]
                    nry += dy[i]
                    if mtrx[nrx][nry] == '#': # 벽인 경우 왔던 방향 그대로 한칸 뒤로 이동
                        nrx -= dx[i]
                        nry -= dy[i]
                        break
                    if mtrx[nrx][nry] == 'O':
                        break
                nbx, nby = bx, by
                while True: # #일 때까지 혹은 구멍일 때까지 움직임
                    nbx += dx[i]
                    nby += dy[i]
                    if mtrx[nbx][nby] == '#': # 벽인 경우 왔던 방향 그대로 한칸 뒤로 이동
                        nbx -= dx[i]
                        nby -= dy[i]
                        break
                    if mtrx[nbx][nby] == 'O':
                        break
                if mtrx[nbx][nby] == 'O': # 파란구슬이 먼저 구멍에 들어가거나 동시에 들어가면 안됨 따라서 이 경우 무시
                    continue
                if nrx == nbx and nry == nby: # 두 구슬의 위치가 같다면
                    if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by): # 더 많이 이동한 구슬이 더 늦게 이동한 구슬이므로 늦게 이동한 구슬 한칸 뒤로 이동
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if (nrx, nry, nbx, nby) not in visited: 
                    q.append((nrx, nry, nbx, nby))
                    visited.append((nrx, nry, nbx, nby))
        count += 1
    print(-1) # 10회가 초과하지 않았지만 10회 내에도 구멍에 들어가지 못하는 경우
bfs(rx, ry, bx, by)