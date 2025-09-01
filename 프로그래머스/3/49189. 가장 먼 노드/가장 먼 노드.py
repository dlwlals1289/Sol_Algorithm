import math
from collections import deque

def solution(n, edge):
    answer = 0
    dq = deque()
    arr = [[]*n for _ in range(n+1)]
    distance = [-1] * (n+1)
    distance[1] = 0
    dq.append(1)
    
    for i in range(len(edge)):
        a, b = edge[i]
        arr[a].append(b)
        arr[b].append(a)
        
    
    while dq:
        now = dq.popleft()
        
        for i in arr[now]:
            if distance[i] == -1:
                distance[i] = distance[now] + 1
                dq.append(i)
            
    answer = distance.count(max(distance))
    
    
    return answer