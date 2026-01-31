# 회의실 배정
import sys
import heapq
input = sys.stdin.readline

N = int(input())
meeting = []
reservation = []
answer = 0

for i in range(N):
    meeting.append(list(map(int, input().split())))
    
meeting.sort(key = lambda x : x[0])

for i in range(N):
    if reservation and reservation[0][0] <= meeting[i][0]:
        heapq.heappop(reservation)
    
    heapq.heappush(reservation, [ meeting[i][1], meeting[i][0] ])

print(len(reservation))