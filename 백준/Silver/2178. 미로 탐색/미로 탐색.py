# 미로 탐색
import sys
from collections import deque
input = sys.stdin.readline

#     좌  우  상  하
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
maze = []
cnt = 1

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
    return maze[n-1][m-1]     

for i in range(n):
    maze.append(list(map(int, input().rstrip())))

print(bfs(0,0))