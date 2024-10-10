# 그림 
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
count = 0
maxSize = 0

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(x, y, size):
    array[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m and array[nx][ny] == 1:
            array[nx][ny] = 0
            size += 1
            size = dfs(nx, ny, size)
    
    return size

for i in range(n):
    for j in range(m):
        size = 1
        if array[i][j] == 1:
            size = dfs(i,j,size)
            count += 1
            if size > maxSize:
                maxSize = size

print(count)
print(maxSize)