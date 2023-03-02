# 하노이의 탑
import sys
input = sys.stdin.readline

n = int(input())

def hanoi(n, fr, to, other):   
    if n == 1:
        print(fr, to)
    else:
        hanoi(n-1, fr, other, to)
        print(fr, to)
        hanoi(n-1, other, to ,fr)

print(2**n-1)
hanoi(n,1,3,2)