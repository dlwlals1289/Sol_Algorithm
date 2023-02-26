# 막대기

import sys

n = int(input())
height = list()

for i in range(n):
    height.append(int(sys.stdin.readline()))

last = height.pop()
result = 1 # 맨 마지막 막대기는 꼭 포함해야 하므로
height.reverse()

for i in height:
    if i > last:
        result += 1
        last = i

print(result)