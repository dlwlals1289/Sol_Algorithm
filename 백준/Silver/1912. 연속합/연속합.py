# 연속합
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
cur = -1000
maxSum = -1000

for num in nums:
    cur = max(num, num+cur)
    maxSum = max(cur, maxSum)
    # print(cur, maxSum)

print(maxSum)