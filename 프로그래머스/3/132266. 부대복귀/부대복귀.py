# 15:45 - 
from collections import deque
def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n+1)]
    
    for road in roads:
        a, b = road
        graph[a].append(b)
        graph[b].append(a)
        
    visited = [False] * (n+1)
    visited[destination] = True
    q = deque([destination])
    dist = [-1] * (n+1)
    dist[destination] = 0
    
    while q:
        now = q.popleft()

        for city in graph[now]:
            if dist[city] == -1:
                dist[city] = dist[now] + 1
                q.append(city)
    
    answer = [dist[s] for s in sources]
    return answer