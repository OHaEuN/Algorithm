from collections import deque

def solution(maps):
    rows = len(maps)
    cols = len(maps[0])
    q = deque([(0,0,1)])
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    visited = [[0 for _ in range(cols)] for _ in range(rows)]
    visited[0][0] = 1
    while q:
        x,y,cnt = q.popleft()
        
        if x == cols-1 and y == rows-1:
            return cnt
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < cols and 0 <= ny and ny < rows:
                if not visited[ny][nx] and maps[ny][nx]:
                    visited[ny][nx] = 1
                    q.append((nx,ny,cnt+1))
    return -1