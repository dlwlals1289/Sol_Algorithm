# 강의실배정
import sys
import heapq
input = sys.stdin.readline

n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
array.sort(key= lambda x : (x[0], x[1]))

heap = []
heapq.heappush(heap, array[0][1])
for i in range(1, n):
    if heap[0] <= array[i][0]:
        heapq.heappop(heap)
    heapq.heappush(heap, array[i][1])

print(len(heap))