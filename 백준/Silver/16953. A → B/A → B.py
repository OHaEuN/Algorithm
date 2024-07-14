import sys
from collections import deque
inputf = sys.stdin.readline

A,B= map(int,inputf().split())
ans = -1
q =deque([(A,1)])
while q:
    n, cnt = q.popleft()
    if n == B:
        ans = cnt
        break
    elif n>B:
        continue     
    else:
        q.append((2*n,cnt+1))
        q.append((int(str(n)+"1"),cnt+1))
print(ans)