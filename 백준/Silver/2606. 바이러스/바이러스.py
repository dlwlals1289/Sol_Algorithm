# 바이러스

import sys
input = sys.stdin.readline

def bfs(graph, start_node):
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

graph = dict()
c_num = int(input())
n_num = int(input())

for i in range(1, c_num+1):
    graph[i] = list()

for i in range(n_num):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

del_list = bfs(graph, 1)
for i in del_list:
    del graph[i]

print(c_num - 1 -len(graph))