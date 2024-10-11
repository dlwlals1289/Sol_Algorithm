# 알파벳
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
route = [list(input().strip()) for _ in range(r)]
visited = [0 for _ in range(26)]
max_count = 0
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(x, y, cnt):
    global max_count
    max_count = max(cnt, max_count) 
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < r and 0 <= ny < c and visited[ord(route[nx][ny]) - ord('A')] == 0:
            visited[ord(route[nx][ny]) - ord('A')] = 1
            dfs(nx, ny, cnt+1)
            visited[ord(route[nx][ny]) - ord('A')] = 0
visited[ord(route[0][0]) - ord('A')] = 1
dfs(0,0,1)
print(max_count)