# 이친수  

N = int(input())
dp = [0 for _ in range(N+1)]
dp[1] = 1

for i in range(N+1):
    if i <= 1:
        continue
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N])