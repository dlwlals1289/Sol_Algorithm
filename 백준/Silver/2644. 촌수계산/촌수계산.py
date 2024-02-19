# 촌수계산
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = []
answer = -1

for _ in range(m):
    x, y = map(int, input().split())
    
    graph[x].append(y)
    graph[y].append(x)

def dfs(v):
    global answer
    if v == b:
        answer = len(visited)
    
    for i in graph[v]:
        if i not in visited:
            visited.append(i)
            dfs(i)
            visited.pop()

dfs(a)
print(answer)