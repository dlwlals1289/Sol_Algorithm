import math 
from collections import deque

def solution(n, wires):
    lenOfWires = len(wires)
    answer = n
    
    arr = [[] for _ in range(n+1)]
    
    def bfs(node):
        dq = deque()
        dq.append(node)
        count = 0
        
        while dq:
            nNode = dq.popleft()
            visited[nNode] = True
            count += 1
            
            for i in arr[nNode]:
                if visited[i] == False:
                    dq.append(i)
        return count
    
    for i in wires:
        a, b, = i
        arr[a].append(b)
        arr[b].append(a)
    
    for i in wires:
        a, b = i
        visited = [False] * (n+1)
        
        arr[a].remove(b)
        arr[b].remove(a)
        
        for j in range(1, n+1):
            if visited[j] == False:
                cnt = bfs(j)
        answer = min(answer, abs((n-cnt) - cnt))
        
        arr[a].append(b)
        arr[b].append(a)
            
    
    return answer