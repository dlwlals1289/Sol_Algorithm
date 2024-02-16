# 섬의 개수
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

flag = True

def dfs(x, y):
    
    dx = [0, 0, -1, 1, -1, -1, 1, 1] # 상하좌우_대각선(좌상,좌하,우하,우상)
    dy = [1, -1, 0, 0, 1, -1, -1, 1]
    
    for i in range(8):
        n_x, n_y = x + dx[i], y + dy[i]
        
        island[x][y] = 0
        if 0 <= n_x < h and 0 <= n_y < w and island[n_x][n_y] == 1:
            dfs(n_x, n_y)
        
        

while flag:
    w, h = map(int, input().split())
    count = 0
    
    if w == 0 and h == 0:
        flag = False
        break
    
    island = [list(map(int, input().split())) for _ in range(h)]
    
    for i in range(h):
        for j in range(w):
            if island[i][j] == 1:
                dfs(i, j)
                count += 1
    
    print(count)