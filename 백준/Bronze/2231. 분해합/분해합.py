# 분해합
import sys

n = int(input())

for i in range(1, n+1):
    A = list(map(int, str(i)))
    sumA = i + sum(A)
    
    if sumA == n:
        print(i)
        break
    if i == n: 
        print(0)