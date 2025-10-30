#테트로미노
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
paper = []
answer = 0

for _ in range(n):
    paper.append(list(map(int, input().split())))

tets = [[(0,1), (0,2), (0,3)], [(1,0), (2,0), (3,0)], # 1x4 형태 
        [(0,1), (1,0), (1,1)], # 2x2형태
        [(1,0),(1,1),(2,1)], [(0,-1), (1,-1), (1,-2)], # ㄹ자 (회전)
        [(1,0), (1,-1), (2,-1)],[(0,1), (1,1), (1,2)], # ㄹ자 (대칭)
        [(1,0), (2,0), (2,1)], [(0,1), (0,2), (1,0)], # ㄴ자 (회전)
        [(0,1),(1,1), (2,1)], [(0,1), (0,2), (-1,2)],
        [(1,0),(2,0),(2,-1)],[(0,1),(0,2),(1,2)], # ㄴ자 (대칭)
        [(1,0),(2,0),(0,1)], [(1,0),(1,1),(1,2)],
        [(1,0),(1,1),(1,-1)], [(1,0),(1,1),(2,0)], # ㅗ자(회전)
        [(0,-1),(1,0),(0,1)],[(0,1),(-1,1),(1,1)] 
]


def calc(i, j, tet):
    tmp = paper[i][j]
    
    for dx, dy in tet:
        nx, ny = i+dx, j+dy
        
        if 0 <= nx < n and 0 <= ny < m:
            tmp += paper[nx][ny]
        else:
            return 0
    return tmp

for i in range(n):
    for j in range(m):
        for tet in tets:
            answer = max(answer, calc(i,j,tet))

print(answer)