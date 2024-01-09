# 색종이
import sys

T = int(input())
answer = 0
paper = [[0]*100 for _ in range(100)]

for _ in range(T):
    left, bottom = map(int, input().split())
    
    for i in range(bottom, bottom+10):
        for j in range(left, left+10):
            if(paper[i][j] == 0):
                answer += 1
                paper[i][j] = 1
    
print(answer)