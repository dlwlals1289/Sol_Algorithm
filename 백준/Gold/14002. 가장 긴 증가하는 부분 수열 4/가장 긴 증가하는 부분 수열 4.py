# 가장 긴 증가하는 수열4
import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
dp = [1 for _ in range(n)] # 수열 길이 저장용
save = [] # 수열 속 원소 저장용

for i in range(n):
    for j in range(i):
        if num[i] > num[j]:
            dp[i] = max(dp[j]+1, dp[i])

index = max(dp)
for i in range(n-1, -1, -1):
    if dp[i] == index:
        save.append(num[i])
        index -= 1

save.reverse()
print(max(dp))
print(*save)