import sys
input = sys.stdin.readline

T =[]
n,m = map(int,input().split())
for _ in range(n):
    T.append(int(input()))
T.sort()

start = min(T)
end = max(T)*m
res = 0
while(start <= end):
    mid = (start+end)//2
    q = 0
    for t in T:
        q += mid // t

    if q >= m:
        end = mid - 1
        res = mid
    else:
        start = mid + 1

print(res)