import sys
input = sys.stdin.readline

n,m = map(int,input().split())
data = list(map(int,input().split()))

vm = max(data)
start = vm
end = sum(data)

res = 10**9
while(start <= end):
    mid = (start+end)//2
    cnt = 1
    tmp = 0
    for i in range(n):
        if(tmp+data[i] <= mid):
            tmp += data[i]
        else:
            cnt += 1
            tmp = data[i]
        if(cnt > m):
            break
    if(cnt > m):
        start = mid+1
    else:
        end = mid-1
        if(mid >= vm):
            res = min(res, mid)

print(res)