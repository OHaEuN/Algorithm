import sys

inputf = sys.stdin.readline

K,N = map(int,inputf().split())
arr=[]
for _ in range(K):
    arr.append(int(input()))

start=1
end=max(arr)

while start<=end:
    mid = (start+end)//2
    cnt = 0
    for n in arr:
        cnt += n//mid
    if cnt >= N:
        start = mid+1
    else:
        end = mid-1
        
print(end)