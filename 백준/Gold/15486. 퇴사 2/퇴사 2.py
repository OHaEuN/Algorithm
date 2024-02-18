import sys
inputf = sys.stdin.readline

N = int(inputf())
t,p = [],[]
dp = [0]*(N+1)
M = 0
for i in range(N):
    x, y = map(int,inputf().split())
    t.append(x)
    p.append(y)
    dp[i] = max(dp[i-1],dp[i])
    M = max(M,dp[i])
    if i+t[i]<=N:
        dp[i+t[i]] = max(M+p[i],dp[i+t[i]])

print(max(dp))