import sys

inputf = sys.stdin.readline
N = int(inputf())
Parr = []
Narr = []
zero = 0

for _ in range(N):
    n = int(inputf())
    if n>0:
        Parr.append(n)
    elif n<=0:
        Narr.append(n)

Parr.sort(reverse=True)
Narr.sort()
ans = 0

def sumGroup(arr):
    global ans
    prev = 0

    for a in arr:
        if a!=1:
            if prev == 0:
                prev = a
            else:
                ans += prev*a
                prev = 0
        else:
            ans += a
    ans += prev

sumGroup(Parr)
sumGroup(Narr)

print(ans)