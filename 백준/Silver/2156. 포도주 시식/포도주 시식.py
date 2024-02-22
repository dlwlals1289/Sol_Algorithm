# 포도주 시식
import sys
input = sys.stdin.readline

n = int(input())
juice = []
answer = [0]*n

for _ in range(n):
    juice.append(int(input()))


answer[0] = juice[0]

for i in range(1, n):
    if i == 1 :
        answer[1] = juice[0]+juice[1]
    elif i == 2:
        answer[2] = max(answer[1], juice[0]+juice[2], juice[1]+juice[2])
    else:       
        answer[i] = max(answer[i-1], answer[i-2]+juice[i], answer[i-3]+juice[i-1]+juice[i])

print(answer[-1])