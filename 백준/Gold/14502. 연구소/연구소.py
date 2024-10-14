# 연구소
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
tmp = [[0]*m for _ in range(n)]
answer = 0

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def infect(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m and tmp[nx][ny] == 0:
            tmp[nx][ny] = 2
            infect(nx, ny)

def count():
    temp = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                temp += 1
    return temp
                
def dfs(w):
    global answer 
    
    if w == 3:
        for i in range(n):
            for j in range(m):
                tmp[i][j] = array[i][j]
                
        for i in range(n):
            for j in range(m):
                if array[i][j] == 2:
                    infect(i,j)
        answer = max(answer, count())
        return
    for i in range(n):
        for j in range(m):
            if array[i][j] == 0:
                array[i][j] = 1
                w += 1
                dfs(w)
                array[i][j] = 0
                w -= 1

dfs(0)
print(answer)