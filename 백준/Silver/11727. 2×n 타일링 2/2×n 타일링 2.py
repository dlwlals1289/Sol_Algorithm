# 2×n 타일링 2

N = int(input())

dp = [0 for _ in range(1001)]
dp[1] = 1
dp[2] = 3

if N > 2:
    for i in range(3, N+1):
        dp[i] = dp[i - 2] * 2 + dp[i -1]

print(dp[N] % 10007)