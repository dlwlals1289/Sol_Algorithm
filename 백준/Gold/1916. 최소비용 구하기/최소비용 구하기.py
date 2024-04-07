# 최소비용 구하기
import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())

bus = [[] for _ in range(n+1)]
dp = [1e9 for _ in range(n+1)]

for i in range(m):
    s, e, p = map(int, input().split())
    bus[s].append([e,p])

start, end = map(int, input().split())

dp[start] = 0

heap = []
heapq.heappush(heap, [0, start])

while heap:
    cost, depart = heapq.heappop(heap)
    
    if dp[depart] < cost:
        continue
    
    for e, p in bus[depart]:
        new_cost = cost+p
        
        if dp[e] > new_cost:
            dp[e] = new_cost
            
            heapq.heappush(heap, [new_cost, e])
        
print(dp[end])