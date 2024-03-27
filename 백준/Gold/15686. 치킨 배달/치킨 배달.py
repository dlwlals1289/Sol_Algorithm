# 치킨 배달
import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
city = []
house = []
chicken = []
answer = 2000 # (50 + 50)*13 보다 큰 수
for i in range(n):
    city.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([i,j])
        elif city[i][j] == 2:
            chicken.append([i,j])

for i in combinations(chicken, m):
    temp = 0
    for h in house:
        distance = 100
        for j in range(m):
            distance = min(distance, abs(h[0]-i[j][0])+abs(h[1]-i[j][1])) # 집과 치킨집 사이 거리 최솟값 구하기
        temp += distance
    answer = min(answer, temp)

print(answer)