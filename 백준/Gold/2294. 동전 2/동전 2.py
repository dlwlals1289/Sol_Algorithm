import sys

n, k = map(int, input().split())
coin = []
dp = [0]*100000

for i in range(n):
    tmp = int(input())
    coin.append(tmp)
    dp[tmp]=1

for c in coin:
    for i in range(c, k+1):
        if dp[i - c] > 0 :
            if dp[i] > 0 :
                dp[i] = min(dp[i-c] + 1, dp[i])
            else:
                dp[i] = dp[i-c] + 1

if dp[k] > 0:
    print(dp[k])  
else:
    print(-1)