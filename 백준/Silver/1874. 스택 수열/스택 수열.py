# 스택 수열
import sys
input = sys.stdin.readline

n = int(input())

stack = list()
answer = list()

cur = 1
index = 0

for i in range(n):
    a = int(input())
    while cur <= a :
        stack.append(cur)
        answer.append("+")
        cur += 1
    
    if stack[-1] == a:
        stack.pop()
        answer.append("-")
        index += 1
    else :
        print("NO")
        break

if index == n:
    for i in range(len(answer)):
        print(answer[i])
