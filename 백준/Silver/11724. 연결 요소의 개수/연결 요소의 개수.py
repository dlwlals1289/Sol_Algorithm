# 연결 요소의 개수

import sys
sys.setrecursionlimit(10000000)

from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
ad_list = [[] for _ in range(n+1)]
visted = [0 for _ in range(n+1)]
cnt = 0

for i in range(m):
    u,v = map(int, input().split())
    
    ad_list[u].append(v)
    ad_list[v].append(u)

def dfs(x):
    visted[x] = 1

    for i in ad_list[x]:
        if not visted[i]:
            dfs(i)

for i in range(1, n+1):
    if visted[i] == 0:
        dfs(i)
        cnt += 1

print(cnt)