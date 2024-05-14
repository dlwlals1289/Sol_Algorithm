# 전깃줄
import sys
input = sys.stdin.readline

n = int(input())

array = []
dp = [1] * n

for i in range(n):
    a, b = map(int, input().split())
    array.append([a,b])

array.sort()

for i in range(1, n):
    for j in range(i):
        if array[i][1] > array[j][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(n - max(dp))