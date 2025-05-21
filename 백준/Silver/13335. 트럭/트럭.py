# 트럭
import sys
from collections import deque

input = sys.stdin.readline

n, w, l = map(int, input().split())
trucks = deque(map(int, input().split()))
bridge = deque([0]*w)
bridgeSum = 0
time = 0


while trucks or bridgeSum >0 :
    time += 1
    
    bridgeSum -= bridge.popleft()
    
    if trucks and bridgeSum + trucks[0] <= l:
        t = trucks.popleft()
        bridgeSum += t
        bridge.append(t)
    else:
        bridge.append(0)

print(time)