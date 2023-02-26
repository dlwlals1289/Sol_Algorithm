# 일곱난쟁이
import sys

result = 0
height = [int(input()) for _ in range(9)]

h_sum = sum(height) - 100

height.sort() # 오름차순 정렬

for i in range(9):
    for j in range(i+1, 9):
        if height[i] + height[j] == h_sum:
            # 제거해야 할 난쟁이 1
            r1 = height[i]
            # 제거해야 할 난쟁이 2
            r2 = height[j]
            
height.remove(r1)
height.remove(r2)

for i in range(7):
    print(height[i])