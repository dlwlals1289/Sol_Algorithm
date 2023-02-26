# 유기농 배추
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(x,y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    graph[x][y] = 0

    for i in range(4):
        if (0 <= (x+dx[i])< m) and (0 <= (y+dy[i]) < n):
            if graph[x+dx[i]][y+dy[i]] == 1:
                graph[x+dx[i]][y+dy[i]] = 0
                dfs(x+dx[i], y+dy[i])

t = int(input())
for i in range(t):
    cnt = 0
    m, n, k = map(int, input().split())
    graph = [[0]*n for _ in range(m)]

    
    for j in range(k): # 데이터 넣기
        a, b = map(int, input().split())
        graph[a][b] = 1
        
    for j in range(m):
        for k in range(n):
            if graph[j][k] == 1:
                dfs(j, k)
                cnt += 1
    print(cnt)