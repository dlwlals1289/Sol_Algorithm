# 평범한 배낭
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
stuff = [[]]
dp = [[0]*(k+1) for _ in range(n+1)]
t_weight = 0

for i in range(n):
    m, v = map(int, input().split())
    stuff.append([m,v])
    
for i in range(1, n+1):
    for j in range(1, k+1):
        n_weight = stuff[i][0]
        n_value = stuff[i][1]
        
        if j < n_weight:
            dp[i][j] = dp[i-1][j] 
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - n_weight] + n_value)

print(dp[n][k])