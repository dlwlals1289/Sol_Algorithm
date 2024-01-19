# N과 M(2)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
visited = [False] * (N+1)
result = []

def dfs():
    if len(result) == M:
        print(' '.join(map(str, result)))
    
    for i in range(1, N+1):
        if i in result:
            continue
        if len(result) > 0 and result[-1] > i:
            continue
        
        result.append(i)
        dfs()
        result.pop()

dfs()