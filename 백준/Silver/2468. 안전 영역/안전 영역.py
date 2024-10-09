# 안전 영역
import sys 
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

N = int(input())
area = []
answer = 0

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(x, y, height):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
            if area[nx][ny] > height:
                visited[nx][ny] = 1
                dfs(nx,ny,height)
            
max_height = 0
for i in range(N):
    area.append(list(map(int, input().split())))
    if max_height < max(area[i]):
        max_height = max(area[i])

for i in range(max_height):
    visited = [[0]*N for _ in range(N)]
    cnt = 0
    
    for j in range(N):
        for k in range(N):
            if area[j][k] > i and visited[j][k] == 0:
                visited[j][k]= 1
                dfs(j,k,i)
                cnt += 1
    
    if cnt > answer:
        answer = cnt

print(answer)