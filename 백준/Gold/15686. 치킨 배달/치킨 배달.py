# 치킨 배달
import sys
from itertools import combinations
import math
input = sys.stdin.readline

n, m = map(int, input().split())
town = []
houses = []
chikens = []
answer = 2*n*n

for _ in range(n):
    town.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if town[i][j] == 1:
           houses.append((i,j))
        elif town[i][j] == 2:
            chikens.append((i,j))

for selected in combinations(chikens, m):
    total = 0
    for r1, c1 in houses:
        distance = 2*n
        
        for r2, c2 in selected:
            distance = min(abs(r1-r2)+abs(c1-c2), distance)
        total += distance
    answer = min(answer, total)
print(answer)