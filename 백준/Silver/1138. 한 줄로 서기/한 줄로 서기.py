# 한 줄로 서기
import sys

N = int(input())

people = list(map(int, input().split()))
temp = [0]*N

for i in range(1, N+1):
    cnt = 0
    
    for j in range(N):
        if cnt == people[i-1] and temp[j] == 0 :
            temp[j] = i
            break
        elif temp[j] == 0:
            cnt = cnt + 1 

print(*temp)