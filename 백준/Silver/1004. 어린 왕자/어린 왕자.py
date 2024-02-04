# 어린왕자

import sys
import math
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    count = 0
    
    n = int(input())
    for i in range(n):
        cx, cy, r = map(int, input().split())
        
        distance1 = math.sqrt(((cx - x1)**2) + ((cy - y1)**2))
        distance2 = math.sqrt(((cx - x2)**2) + ((cy - y2)**2))
        
        if distance1 <= r and distance2 > r:
            count += 1
        if distance2 <= r and distance1 > r:
            count += 1
    
    print(count)