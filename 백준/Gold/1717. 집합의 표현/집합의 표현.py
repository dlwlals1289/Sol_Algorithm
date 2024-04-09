# 집합의 표현 
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, m = map(int, input().split())

p = [i for i in range(n+1)]

def find(x):
    if p[x] == x:
        return x
    p[x] = find(p[x])
    return p[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a <= b:
        p[b] = a
    else:
        p[a] = b

for i in range(m):
    op, a, b = map(int, input().split())
    
    if op == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")