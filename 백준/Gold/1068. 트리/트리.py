# 트리
import sys
input = sys.stdin.readline

n = int(input())
parent = list(map(int, input().split()))
d_node = int(input())

def dfs(node):
    parent[node] = -2
    
    for i in range(n):
        if node == parent[i]:
            dfs(i)
dfs(d_node)

count = 0
for i in range(n):
    if parent[i] != -2 and i not in parent:
        count += 1

print(count)