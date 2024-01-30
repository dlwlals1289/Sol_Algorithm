# 회전하는 큐

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
queue = deque([i for i in range(1, N+1)])

target = list(map(int, input().split()))
answer = 0
for i in range(M):
    index = queue.index(target[i])
    
    if (len(queue)/2) >= index:
        answer += index
        queue.rotate(-index)
        queue.popleft()

    else:
        answer += (len(queue) - index)
        queue.rotate(len(queue) - index)
        queue.popleft()

print(answer)