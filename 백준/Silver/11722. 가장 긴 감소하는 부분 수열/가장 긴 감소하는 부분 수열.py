import sys
inputf = sys.stdin.readline

N = int(inputf().rstrip())
arr = list(map(int,inputf().split()))
cnt = [1 for _ in range(N)]

for i in range(N):
    prev = 0
    for j in range(i):
        if arr[j]>arr[i]:
            prev = max(prev,cnt[j])
    cnt[i] = prev+1

print(max(cnt))