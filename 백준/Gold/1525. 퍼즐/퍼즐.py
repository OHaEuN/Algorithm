import sys
from collections import deque
inputf = sys.stdin.readline

graph = ""
ans = "123456780"
for _ in range(3):
    graph += ''.join(list(inputf().split()))

move=[(-1,0),(1,0),(0,1),(0,-1)]
visited = {graph: 0}
q = deque([graph])
while q:
    prev = q.popleft()
    count = visited[prev]
    zero = prev.index("0")
    
    if prev == "123456780":
        print(count)
        quit()

    x = zero//3
    y = zero%3
    count+=1
    for i,j in move:
        nx = x+i
        ny = y+j
        if 0<=nx<3 and 0<=ny<3:
            nz = nx*3 +ny
            cur = list(prev)
            cur[nz],cur[zero] = cur[zero],cur[nz]
            cur = ''.join(cur)

            if cur not in visited:
                visited[cur] = count
                q.append(cur)
print(-1)