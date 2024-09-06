# 로봇청소기
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = []
answer = 1
vistied = [[0]*M for _ in range(N)]

dx = [0, 1, 0, -1] 
dy = [-1, 0, 1, 0] 
for _ in range(N):
    room.append(list(map(int, input().split())))

vistied[r][c] = 1 # 첫 방은 방문표시       
while True:
    flag = 0
    
    for i in range(4):
        d = (d+3)%4
        nr = r + dy[d]
        nc = c + dx[d]
        
        if 0 <= nr < N and 0 <= nc < M and room[nr][nc] == 0: # 범위 안이며 청소해야 하면
            if vistied[nr][nc] == 0: # 방문하지 않았다면
                vistied[nr][nc] = 1
                r = nr
                c = nc
                answer += 1
                flag = 1
                break
        
    if flag == 0: # 청소 안 했으면
        if room[r - dy[d]][c - dx[d]] == 1: # 후진했는데 벽이면
            break
        else:
            r = r - dy[d]
            c = c - dx[d]
print(answer)