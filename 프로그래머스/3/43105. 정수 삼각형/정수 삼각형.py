def solution(triangle):
    answer = 0
    n = len(triangle)
    dp = [[] for _ in range(n)]
    dp[0].append(triangle[0][0])
    
    for i in range(1, n):
        m = len(triangle[i])
        for j in range(m):
            if j == 0:
                dp[i].append(triangle[i][0] + dp[i-1][0])
            elif j == m-1:
                dp[i].append(triangle[i][j] + dp[i-1][j-1])
            else:
                dp[i].append(triangle[i][j] + max(dp[i-1][j], dp[i-1][j-1]))

    return max(dp[-1])