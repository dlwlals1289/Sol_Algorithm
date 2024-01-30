# 01타일

import sys
input = sys.stdin.readline

N = int(input())

dp = [0 for _ in range(N+1)]

for i in range(N):
    if i < 2:
        dp[i] = i + 1
        continue
    dp[i] = (dp[i-2] + dp[i-1])%15746

print(dp[N-1])