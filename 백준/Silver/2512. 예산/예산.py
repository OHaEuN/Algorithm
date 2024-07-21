import sys

inputf = sys.stdin.readline

N = int(inputf())
arr = list(map(int, inputf().split()))
M = int(inputf())

s, e = 0, max(arr)
ans = 0

while s <= e:
    mid = (s + e) // 2
    cnt = 0
    for i in arr:
        cnt += min(i, mid)
    
    if cnt <= M:
        ans = mid
        s = mid + 1
    else:
        e = mid - 1

print(ans)