import sys
import bisect
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
dp = [0 for _ in range(n)]
cp = [-float('inf')] # 문제의 조건에 음수가 포함되므로 최저를 0이 아닌 -무한대로 설정해준다.
for i in range(0,n):
    if a[i] > cp[-1]:
        cp.append(a[i])
        dp[i] = len(cp) -1
    else:
        dp[i] = bisect.bisect_left(cp,a[i])
        cp[dp[i]] = a[i]
print(len(cp)-1)

max_idx, ans = max(dp) + 1,[]
for i in range(n-1,-1,-1):
    if dp[i] == max_idx -1 : 
        ans.append(a[i])
        max_idx = dp[i]
print(*ans[::-1])