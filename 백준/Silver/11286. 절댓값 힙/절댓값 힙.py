# 절댓값 힙
import sys
import heapq
input = sys.stdin.readline

N = int(input())
hq = []
    
for i in range(N):
    num = int(input())
    
    if num == 0:
        if not hq:
            print(0)
        else:
            absNum, n = heapq.heappop(hq)
            print(n)
    else:
        heapq.heappush(hq, (abs(num), num))