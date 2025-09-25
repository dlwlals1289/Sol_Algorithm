from collections import deque
def bfs(table, target):
    n = len(table)
    visited = [[False]*n for _ in range(n)]
    blocks = []
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and table[i][j] == target:
                q = deque([(i,j)])
                visited[i][j] = True
                shape = []
            
                while q:
                    x, y = q.popleft()
                    shape.append((x,y))

                    for dx, dy in [(0,1), (0, -1), (1,0), (-1,0)]:
                        nx, ny = x+dx, y+dy

                        if 0 <= nx and nx < n and 0 <= ny and ny < n and not visited[nx][ny] and table[nx][ny] == target:
                            visited[nx][ny] = True
                            q.append((nx,ny))
                blocks.append(shape)
    return blocks

def normalize(shape):
    min_x = min(x for x, y in shape)
    min_y = min(y for x, y in shape)
    
    return sorted([(x-min_x, y-min_y)for x, y in shape])
        
def rotate(shape):
    rotated = [(y, -x) for x, y in shape]
    return normalize(rotated)

def get_rotations(shape):
    rotations = []
    cur = normalize(shape)
    for _ in range(4):
        rotations.append(cur)
        cur = rotate(cur)
    return rotations

def solution(game_board, table):
    answer = 0
    shapes = []
    
    empty_blocks = [ normalize(shape) for shape in bfs(game_board, 0)]
    puzzle_blocks = [ normalize(shape) for shape in bfs(table, 1)]
    
    used = [False] * len(puzzle_blocks)
    
    for empty in empty_blocks:
        for i, puzzle in enumerate(puzzle_blocks):
            if used[i] or len(puzzle) != len(empty):
                continue
                
            for rotation in get_rotations(puzzle):
                if empty == rotation:
                    used[i] = True
                    answer += len(puzzle)
                    break
            if used[i]:
                break
                

    return answer