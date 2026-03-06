# 추월
import sys
from collections import deque, defaultdict
input = sys.stdin.readline

n = int(input())

in_order = deque([input().rstrip() for _ in range(n)])
out_order = deque([input().rstrip() for _ in range(n)])
answer = 0

for i in range(n):
    if in_order[0] == out_order[i]:
        in_order.popleft()
    else:
        answer += 1
        del in_order[in_order.index(out_order[i])]
print(answer)