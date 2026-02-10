#색종이-3
import sys
input = sys.stdin.readline

T = int(input())
paper = [[0]*101 for _ in range(101)]
answer = 0

for _ in range(T):
    x, y = map(int, input().split())
    
    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = 1

for i in range(101):
    for j in range(101):
        if paper[i][j] != 0 and paper[i+1][j] != 0:
            paper[i+1][j] = paper[i][j] + 1

for i in range(101):
    for j in range(101):
        h = 100

        for k in range(j, 101):
            h = min(h, paper[i][k])
            
            if h == 0:
                break
            
            answer = max(answer, h*(k-j+1))
            
print(answer)