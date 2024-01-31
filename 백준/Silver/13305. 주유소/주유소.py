# 주유소

import sys
input = sys.stdin.readline

N = int(input())
distance = list(map(int, input().split()))
oilPrice = list(map(int, input().split()))

lowPrice = min(oilPrice[:N-1])
l_PriceIndex = oilPrice.index(lowPrice)

answer = 0
for i in range(l_PriceIndex):
    answer += distance[i] * oilPrice[i]
answer += sum(distance[l_PriceIndex:]) * lowPrice

print(answer)