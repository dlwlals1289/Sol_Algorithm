# 최단거리
import sys
from heapq import heappush, heappop
from collections import deque
input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input())

graph = [[] for _ in range(V+1)]

for i in range(E):
    u, v, w = map(int, input().split())
    
    graph[u].append([v,w])

visited = [False]*(V+1)
INF = float('inf')
answer = [INF] * (V+1)
q = [[0, start]]

while q:
    total, now = heappop(q)
    
    if total >= answer[now]:
        continue
    answer[now] = total
    
    for nxt, w in graph[now]:
        heappush(q, [total+w, nxt])
        
for i in range(1, V+1):
    if answer[i] == INF:
        print("INF")
        continue
    print(answer[i])