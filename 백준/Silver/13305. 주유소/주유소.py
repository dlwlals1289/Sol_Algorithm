# 주유소

import sys
input = sys.stdin.readline

N = int(input())
distance = list(map(int, input().split()))
oilPrice = list(map(int, input().split()))

minPrice = oilPrice[0]

answer = 0

for i in range(N-1):
    if minPrice > oilPrice[i]:
        minPrice = oilPrice[i]
    answer += (distance[i] * minPrice)
    
print(answer)