# 수 찾기
import sys
input=sys.stdin.readline

n = int(input())
A = set(map(int, input().split()))

m = int(input())
find = list(map(int, input().split()))

for i in find:
    if i in A:
        print(1)
    else:
        print(0)