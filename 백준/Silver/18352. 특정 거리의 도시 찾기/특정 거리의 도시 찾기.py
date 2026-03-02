# 특정 거리의 도시 찾기
import sys
from collections import deque

input = sys.stdin.readline
n, m, k, x = map(int, input().split())
roads = [[] for _ in range(n+1)]
arr = [-1]*(n+1)

for i in range(m):
    depart, dest = map(int, input().split())
    roads[depart].append(dest)

dq = deque([])
dq.append((x,0))
arr[x] = 0

while dq:
    city, dist = dq.popleft()
    
    for i in roads[city]:
        if arr[i] == -1:
            arr[i]= dist + 1
            dq.append((i, dist+1))

if k not in arr:
    print(-1) 
else:
    for i, dist in enumerate(arr):
        if dist == k:
            print(i)