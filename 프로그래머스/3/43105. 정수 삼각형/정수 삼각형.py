def solution(triangle):
    answer = 0
    h = len(triangle)
    dp = [[0]*(i+1) for i in range(h)]
    dp[0][0] = triangle[0][0]
    
    for i in range(h-1):
        for c in range(i+1):
            dp[i+1][c] = max(dp[i+1][c], triangle[i+1][c] + dp[i][c])
            dp[i+1][c+1] = max(dp[i+1][c+1], triangle[i+1][c+1] + dp[i][c])
            
    return max(dp[h-1])