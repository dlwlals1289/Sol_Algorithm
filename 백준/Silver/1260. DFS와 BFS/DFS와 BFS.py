# DFS와 BFS
import sys
from collections import deque
input = sys.stdin.readline

n,m,v = map(int, input().split())
visited = [False for _ in range(n+1)]
arr = [[] for _ in range(n+1)]
result = []
result2 = []

for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in arr:
    i.sort()
    

def dfs(x) :
    visited[x] = True
    result.append(x)
    for i in arr[x]:
        if visited[i]:
            continue
        dfs(i)

dfs(v)
print(" ".join(map(str, result)))


visited = [False for _ in range(n+1)]
def bfs(x):
    tmp = deque()
    tmp.append(x)
    visited[x] = True
    
    while len(tmp) != 0 :
        target = tmp.popleft()
        result2.append(target)
        
        for i in arr[target]:
            if visited[i] :
                continue

            tmp.append(i)
            visited[i] = True

bfs(v)
print(" ".join(map(str, result2)))
        