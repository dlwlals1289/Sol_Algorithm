def solution(land):
    answer = 0
    row = len(land)
    col = len(land[0])
    
    dp = [[0]*col for _ in range(row)]
    
    for i in range(row):
        for j in range(col):
            if i == 0:
                dp[i][j] = land[i][j]
            else:
                for k in range(col):
                    if k != j:
                        dp[i][j] = max(dp[i][j], land[i][j] + dp[i-1][k])
            
    return max(dp[-1])