#색종이2
import sys
input = sys.stdin.readline

t = int(input())
grid = [[0]*101 for _ in range(101)]  # 여유

for _ in range(t):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            grid[i][j] = 1

answer = 0
dir = [(1,0), (0, -1), (-1, 0), (0, 1)]

for i in range(101):
    for j in range(101):
        if grid[i][j]:
            for dx, dy in dir:
                nx, ny = i + dx, j + dy
                
                if nx < 0 or 100 < nx or ny < 0 or 100 < ny or grid[nx][ny] == 0:
                    answer += 1
print(answer)