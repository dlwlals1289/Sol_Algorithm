from collections import deque
def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n+1)]
    dist_from_dest = [-1 for _ in range(n+1)]
    
    for road in roads:
        a, b = road
        graph[a].append(b)
        graph[b].append(a)
        
    q = deque([])
    q.append((destination,0))
    dist_from_dest[destination] = 0

    while q:
        node, dist = q.popleft()

        for next_node in graph[node]:
            if dist_from_dest[next_node] == -1:
                dist_from_dest[next_node] = dist + 1
                q.append((next_node, dist+1))
    
    for source in sources:
        answer.append(dist_from_dest[source])
        
    return answer