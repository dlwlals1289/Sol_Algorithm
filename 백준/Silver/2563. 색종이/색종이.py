# 색종이
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

t = int(input())
paper = [[0] * 101 for _ in range(101)]
answer = 0

for _ in range(t):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = 1

for i in range(1, 101):
    for j in range(1, 101):
        if paper[i][j] == 1:
            answer += 1

print(answer)