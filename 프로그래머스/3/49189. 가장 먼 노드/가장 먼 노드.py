from collections import deque, Counter
def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    dist = [-1 for _ in range(n+1)]
    q = deque([1])
    dist[1] = 0

    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    
    
    while q:
        node = q.popleft()
        
        for i in graph[node]:
            if dist[i] == -1:
                q.append(i)
                dist[i] = dist[node] + 1
                
    cnt = Counter(dist)
    answer = cnt[max(dist)]
    return answer