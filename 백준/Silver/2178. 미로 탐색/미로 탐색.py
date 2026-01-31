# 미로 탐색
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]
answer = 1

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
visited = [[False] * M for _ in range(N)]

q = deque()
q.append((0,0))
visited[0][0] = True

while q:
    x, y = q.popleft()
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx] and maze[ny][nx] != 0:
            q.append((nx, ny))
            visited[ny][nx] = True
            maze[ny][nx] = maze[y][x] + 1

print(maze[N-1][M-1])