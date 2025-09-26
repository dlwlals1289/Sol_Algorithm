from collections import deque
import math

    
def solution(n, wires):
    answer = n
    
    tree = [[]*(n+1) for _ in range(n+1)]
    for a, b in wires:
        tree[a].append(b)
        tree[b].append(a)
    
    
    def bfs(node):
        nonlocal answer
        q = deque()
        visited = [False]*(n+1)
        q.append(node)
        visited[node] = True
        cnt = 0
        
        while q:
            now = q.popleft()
            cnt += 1
            
            for next in tree[now]:
                if not visited[next]:
                    q.append(next)
                    visited[next] = True
        
        answer = min(answer, abs(n-cnt*2))

    
    for a, b in wires:
        tree[a].remove(b)
        tree[b].remove(a)
        
        for i in tree:
            if i != []:
                bfs(i[0])
                break
        tree[a].append(b)
        tree[b].append(a)
    return answer