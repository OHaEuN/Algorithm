import sys

inputf=sys.stdin.readline

T = int(inputf())
for _ in range(T):
    N, M = map(int,inputf().split())
    q = list(map(int,inputf().split()))
    ans = 1
    cnt = 0
    while q:
        max_n = max(q)
        cur = q.pop(0)
        if max_n == cur:
            cnt+=1
            if M == 0:
                print(cnt)
                break
        else:
            q.append(cur)
            if M == 0:
                M = len(q)
        M -= 1