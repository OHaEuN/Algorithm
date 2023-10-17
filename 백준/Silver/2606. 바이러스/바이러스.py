import sys
inputf= sys.stdin.readline
N = int(inputf())
n = int(inputf())
net = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
for _ in range(n):
    a,b = map(int,inputf().split())
    net[a].append(b)
    net[b].append(a)
queue = [1]
while queue:
    v = queue.pop(0)
    visited[v] = 1
    for i in net[v]:
        if visited[i] == 0:
            queue.append(i)
count = 0
for i in visited:
    if i == 1:
        count+=1
print(count-1)