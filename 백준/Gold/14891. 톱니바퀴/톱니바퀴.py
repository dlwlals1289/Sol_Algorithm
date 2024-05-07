#톱니바퀴
import sys
from collections import deque
input = sys.stdin.readline

cog = [deque(list(map(int, input().rstrip()))) for _ in range(4)]
k = int(input())

for _ in range(k):
    n, d = map(int, input().split())
    save = [0,0,0]
    for i in range(3):
        if cog[i][2] != cog[i+1][6]:
            save[i] = 1

    for l in range(n-1, 0, -1):
        if save[l-1] == 0:
            break
        else:
            l_d = int((-1)**(n-l))
            cog[l-1].rotate(l_d*d)
            
    for r in range(n-1, 3):
        if save[r] == 0:
            break
        else:
            r_d = int((-1)**(r-n))
            cog[r+1].rotate(r_d*d)
        
    cog[n-1].rotate(d)

answer = 0
for i in range(4):
    if cog[i][0] == 1:
        answer += 2**(i)
print(answer)