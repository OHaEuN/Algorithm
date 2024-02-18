import sys
inputf = sys.stdin.readline

N = int(inputf())
arr = list(inputf().strip())
dp = [float("inf")]*N
dp[0] = 0
for i in range(1,N):
    for j in range(i):
        if arr[j] == "B" and arr[i] != "O":
            continue
        elif arr[j] == "O" and arr[i] != "J":
            continue
        elif arr[j] == "J" and arr[i] != "B":
            continue
        dp[i] = min(dp[i],dp[j]+(i-j)**2)

if dp[N-1] == float("inf"):
    print(-1)
else:
    print(dp[N-1])