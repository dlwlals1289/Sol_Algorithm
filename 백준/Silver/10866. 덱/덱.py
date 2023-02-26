# deq

# 큐

import sys
from collections import deque

n = int(input())
deq = deque([])

for i in range(n):
    a = list(sys.stdin.readline().split())
    if a[0] == 'push_front':
        deq.appendleft(a[1])
    if a[0] == 'push_back':
        deq.append(a[1])
    if a[0] == 'pop_front':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.popleft())
    if a[0] == 'pop_back':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.pop())
    if a[0] == 'size':
        print(len(deq))
    if a[0] == 'empty':
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    if a[0] == 'front':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
    if a[0] == 'back':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])
