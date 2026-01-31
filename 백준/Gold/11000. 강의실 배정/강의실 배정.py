# 강의실 배정
import sys
import heapq
input = sys.stdin.readline

N = int(input())
lesson = [list(map(int, input().split())) for _ in range(N)]
lesson.sort(key = lambda x : x[0])

rooms = []

for i in range(N):
    if rooms and rooms[0] <= lesson[i][0]:
        heapq.heappop(rooms)
    heapq.heappush(rooms, lesson[i][1])
print(len(rooms))