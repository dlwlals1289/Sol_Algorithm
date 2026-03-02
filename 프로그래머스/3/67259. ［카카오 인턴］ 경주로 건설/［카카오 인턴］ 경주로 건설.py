from heapq import heappush, heappop

def solution(board):
    answer = 0
    dq = []
    n = len(board)
    INF = float('inf')
    arr = [[[INF]*4 for _ in range(n)] for _ in range(n)]
    
    heappush(dq, (0,0,0,0)) #cost, x, y, dir
    heappush(dq, (0,0,0,3))
    
    dx = [1, 0, -1, 0] # 우상좌하 -> 0123
    dy = [0, -1, 0, 1]
    
    arr[0][0][0] = 0
    arr[0][0][3] = 0
    while dq:
        cost, x, y, d = heappop(dq)
        
        if cost > arr[x][y][d]:
            continue
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 1:
                new_cost = cost
                
                if d == i: # 진행방향이 이전과 같은 경우
                    new_cost = cost+100
                else: # 진행방향이 다른 경우
                    new_cost = cost+600
                if arr[nx][ny][i] > new_cost:
                    arr[nx][ny][i] = new_cost
                    heappush(dq, (new_cost, nx, ny, i))
        
    return min(arr[n-1][n-1])