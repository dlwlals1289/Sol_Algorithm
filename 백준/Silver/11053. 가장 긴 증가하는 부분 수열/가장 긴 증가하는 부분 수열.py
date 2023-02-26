# 가장 긴 증가하는 부분 수열
import sys
n = int(input())

num = list(map(int, sys.stdin.readline().split()))

d = [0]*n

for i in range(n):
    for j in range(i):
        if num[i] > num[j] and d[i] < d[j] :
            d[i] = d[j]
    d[i] += 1

print(max(d))