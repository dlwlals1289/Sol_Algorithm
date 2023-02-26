# 치킨 TOP N

import sys

n = int(input())
chicken = list(map(int, input().split()))
k = int(input())

index = n // k
arr = list()
result = list()
for i in range(0, n, index):
    arr = chicken[i:i+index]
    arr.sort()
    for j in arr:
        result.append(j)

print(*result)