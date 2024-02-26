# 가장 큰 증가하는 부분 수열
import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
dp = [0 for _ in range(n)]
dp = num[:]


for i in range(1, n):
    for j in range(i):
        if num[j] < num[i]:
            dp[i] = max(dp[i], dp[j]+num[i])

print(max(dp))