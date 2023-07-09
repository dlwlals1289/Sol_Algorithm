# 토마토
import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

m, n = map(int, input().split())
box = [] # 토마토박스
visited = [[0]*m for i in range(n)] # 방문 여부
queue = deque()
cnt = 0

for i in range(n):
    box.append(list(map(int, input().split())))
    
for i in range(n):
    for j in range(m):
        if(box[i][j] == 1):
            queue.append((i,j))
            visited[i][j] = 1 
while(queue):
    for k in range(len(queue)):
        x = queue[0][0]
        y = queue[0][1]
        queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m :
                if visited[nx][ny] == 0 and box[nx][ny] != -1 : # 방문한 적 없고 토마토가 있는 곳
                    queue.append((nx,ny))
                    box[nx][ny] = 1
                    visited[nx][ny] = 1
    cnt = cnt + 1

answer = True
for i in range(n):
    for j in range(m):
        if box[i][j] == 0 :
            answer = False
            break
    
if answer == True:
    print(cnt-1)
else :
    print(-1)