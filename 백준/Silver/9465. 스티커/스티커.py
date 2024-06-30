import sys
inputf = sys.stdin.readline

T = int(inputf().rstrip())
for _ in range(T):
    N = int(inputf().rstrip())
    arr = []
    for _ in range(2):
        arr.append(list(map(int,inputf().split())))
    dp = arr[:]

    if N == 1:
        print(max(dp[0][0],dp[1][0]))
        continue

    dp[0][1] = arr[1][0] + arr[0][1]
    dp[1][1] = arr[0][0] + arr[1][1]
    for x in range(2,N):
        dp[0][x] = max(dp[1][x-2],dp[1][x-1]) + arr[0][x]
        dp[1][x] = max(dp[0][x-2],dp[0][x-1]) + arr[1][x]
    
    print(max(dp[0][N-1], dp[1][N-1]))