import sys
from collections import deque

inputf = sys.stdin.readline

N = int(inputf())
graph = [[] for _ in range(N+1)]
ans = [0]*(N+1)
for _ in range(N-1):
    a,b = map(int,inputf().split())
    graph[a].append(b)
    graph[b].append(a)

q =deque([1])
while q:
    i = q.popleft()
    for x in graph[i]:
        if not ans[x]:
            ans[x] = i
            q.append(x)

for i in range(2,N+1):
    print(ans[i])