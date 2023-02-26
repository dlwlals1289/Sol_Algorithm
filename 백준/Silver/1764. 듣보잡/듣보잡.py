# 듣보잡
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

set1 = set()
set2 = set()

for i in range(n):
    a = input().rstrip()
    set1.add(a)

for i in range(m):
    a = input().rstrip()
    set2.add(a)

set3 = list(set1 & set2)
set3.sort()

print(len(set3))
for i in range(len(set3)):
    print(set3[i])
