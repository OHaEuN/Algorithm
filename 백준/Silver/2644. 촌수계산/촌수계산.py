import sys
from collections import deque
inputf = sys.stdin.readline

N = int(inputf())
graph = [[] for _ in range(N+1)]
X,Y = map(int,inputf().split())
M = int(inputf())
for _ in range(M):
    a,b = map(int,inputf().split())
    graph[a].append(b)
    graph[b].append(a)

ans = -1
q = deque([(X,0)])
visited = [0 for _ in range(N+1)]
while q:
    x, cnt = q.popleft()
    for i in graph[x]:
        if i and not visited[i]:
            if i == Y:
                ans = cnt+1
                break
            else:
                q.append((i,cnt+1))
                visited[i] = 1
print(ans)