import sys

inputf = sys.stdin.readline
N, M = map(int, inputf().split())

if N == 1:
    ans = 1
elif N == 2:
    ans = min(4, (M-1)//2 + 1)
elif M < 7:
    ans = min(4, M)
else:
    ans = (2 + (M-5)) + 1
print(ans)