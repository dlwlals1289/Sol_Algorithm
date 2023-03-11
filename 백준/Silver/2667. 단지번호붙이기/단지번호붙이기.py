# 단지번호 붙이기

import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
visited = [[0]*n for _ in range(n)] # 방문 노드 기록용
array = []

count = []

def dfs(x, y):
    deq = deque()
    deq.append((x,y))
    cnt = 1
    
    while deq:
        x, y = deq.popleft() 
        visited[x][y] = 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and array[nx][ny] == 1 and visited[nx][ny] == 0:
                deq.append((nx, ny))
                visited[nx][ny] = 1   
                cnt += 1

    return cnt

for i in range(n):
    array.append(list(map(int, input().rstrip())))

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and array[i][j] == 1:
            count.append(dfs(i,j))
            
count.sort()
print(len(count))
for i in range(len(count)):
    print(count[i])