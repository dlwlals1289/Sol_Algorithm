from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    array = [[-1]*102 for _ in range(102)]
    visited = [[1]*102 for _ in range(102)]
    
    for r in rectangle:
        lbx, lby, rtx, rty = map(lambda x : x*2, r)
        for i in range(lbx, rtx+1):
            for j in range(lby, rty+1):
                if lbx < i < rtx and lby < j < rty:
                    array[i][j] = 0
                elif array[i][j] != 0:
                    array[i][j] = 1
    route = deque()
    route.append((characterX*2, characterY*2))
    
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    while route:
        x, y = route.popleft()
        
        if x == itemX*2 and y == itemY*2:
            answer = visited[x][y] //2
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < 102 and 0 <= ny < 102 and visited[nx][ny] == 1:
                if array[nx][ny] == 1:
                    route.append((nx,ny))
                    visited[nx][ny] += visited[x][y]
        
    return answer