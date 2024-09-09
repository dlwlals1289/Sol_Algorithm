# 스타트와 링크
import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
index = [i for i in range(N)]
min = 40000

for s in combinations(index, N//2):
    start = 0 
    link = 0

    for i in combinations(s, 2):
        start += arr[i[0]][i[1]]
        start += arr[i[1]][i[0]]
        
    l = list(set(index) - set(s))
    for i in combinations(l, 2):
        link += arr[i[0]][i[1]]      
        link += arr[i[1]][i[0]]      
        
    if abs(start - link) < min:
        min = abs(start - link)
print(min)