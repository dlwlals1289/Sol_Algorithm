#적록색약
from collections import deque


n = int(input())

def bfs(a,b):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0] # 상하좌우
    
    stack.append((a,b))
    color = area[a][b]
    visited[a][b] = 1
    
    while(stack):
        x, y = stack.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and area[nx][ny] == color and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                stack.append((nx, ny))


area = []
stack = deque()
for i in range(n):
    area.append(list(input().rstrip()))

# 적록색맹 아닌 경우
visited = [[0]*n for _ in range(n)]
cnt1 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i,j)
            cnt1 += 1
            
# 적록색맹인 경우
visited = [[0]*n for _ in range(n)]
cnt2 = 0

for i in range(n):
    for j in range(n):
        if area[i][j] == 'G':
            area[i][j] = 'R'
            
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i,j)
            cnt2 += 1
            
print(cnt1, cnt2)
