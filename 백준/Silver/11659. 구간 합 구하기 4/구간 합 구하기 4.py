# 구간 합 구하기(4)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
number = list(map(int, input().split()))
number.insert(0, 0)

sum = [0 for _ in range(N+1)]

for i in range(1, N+1):
    sum[i] = sum[i-1] + number[i]

for i in range(M):
    start, end = map(int, input().split())
    print(sum[end] - sum[start - 1])