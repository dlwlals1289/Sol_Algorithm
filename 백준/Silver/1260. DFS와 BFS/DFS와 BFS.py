# DFS와 BFS
import sys
input = sys.stdin.readline

def dfs_recursive(graph, start, visited = []): # DFS

    visited.append(start)
 
    for node in graph[start]:
        if node not in visited:
            dfs_recursive(graph, node, visited)
    return visited

def bfs(graph, start_node): # BFS
    need_visited, visited = [], []
    need_visited.append(start_node)

    while need_visited:
        node = need_visited[0]
        del need_visited[0]

        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
            # print(need_visited)
    return visited

n,m,v = map(int, input().split())

graph = [[]*n for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

print(*dfs_recursive(graph, v))
print(*bfs(graph, v))