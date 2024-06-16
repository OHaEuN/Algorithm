import sys

inputf = sys.stdin.readline
N = inputf().rstrip()

if "0" not in N:
    print(-1)
else:
    t = 0
    for i in range(len(N)):
        t += int(N[i])

    if t % 3 != 0:
        print(-1)
    else:
        sortedN = sorted(N, reverse=True)
        ans = "".join(sortedN)
        print(ans)