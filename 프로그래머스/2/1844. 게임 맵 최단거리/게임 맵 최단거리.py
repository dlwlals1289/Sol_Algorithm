from collections import deque
import math

def solution(maps):
    answer = 0
    # n, m = len(maps[0]), len(maps)
    n, m = len(maps), len(maps[0])
    dq = deque()
    dq.append([0,0])
    maps[0][0] = 0
    
    dist = [[0]*m for _ in range(n)]
    dist[0][0] = 1
    
    
    dx = [0, -1, 0, 1] 
    dy = [1, 0, -1, 0]
    
    while dq:
        x, y = dq.popleft()
        
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                dq.append([nx, ny])
                maps[nx][ny] = 0
                if dist[nx][ny] != 0:
                    dist[nx][ny] = min(dist[nx][ny], dist[x][y]+1)
                    continue
                dist[nx][ny] = dist[x][y]+1
    
    if dist[n-1][m-1] == 0 :
        answer = -1
    else :
        answer = dist[n-1][m-1]
                
    return answer