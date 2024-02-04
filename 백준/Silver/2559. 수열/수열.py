# 수열

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

temp = list(map(int, input().split()))
result = []
result.append(sum(temp[:K]))

for i in range(1, N - K + 1):
    result.append(result[i-1] - temp[i-1] + temp[i + K - 1])

print(max(result))