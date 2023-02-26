# 제로
import sys

n = int(input())

stack = []

for i in range(n):
    a = int(sys.stdin.readline())
    if a == 0:
        stack.pop()
    else:
        stack.append(a)

result = sum(stack)
print(result)
