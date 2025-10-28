import math
from collections import deque
def solution(n, wires):
    answer = n
                
    for i in range(n-1):
        arr = [[] for _ in range(n+1)]
        visited = [False] *(n+1)
        
        for j in range(n-1):
            if i != j:
                v1, v2 = wires[j][0], wires[j][1]

                arr[v1].append(v2)
                arr[v2].append(v1)

        q = deque([1])
        visited[1] = True
        
        tmp = 0
        while q:
            node = q.popleft()
            tmp += 1
            
            for i in arr[node]:
                if not visited[i]:
                    visited[i] = True
                    q.append(i)

        answer = min(abs(2*tmp - n), answer)
            
    return answer