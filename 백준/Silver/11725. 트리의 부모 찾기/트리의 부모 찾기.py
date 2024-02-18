# 트리의 부모 찾기
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8) #재귀 리미트

n = int(input())
graph =[[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)] 

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(i):
    for j in graph[i]:
        if not visited[j]:
            visited[j] = i
            dfs(j)

dfs(1)      

for i in range(2, n+1):
    print(visited[i])