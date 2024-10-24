# 절댓값 힙
import sys
import heapq
input = sys.stdin.readline

n = int(input())
abs_array = []

for i in range(n):
    num = int(input())
    
    if num:
        heapq.heappush(abs_array, (abs(num), num))
    else:
        if abs_array:
            min = heapq.heappop(abs_array)[1]
            print(min)
        else:
            print(0)