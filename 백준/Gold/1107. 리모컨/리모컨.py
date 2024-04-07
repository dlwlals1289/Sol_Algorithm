# 리모컨
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
n_working = list(map(int, input().split()))

count = abs(100 - n)

for num in range(1000001):
    num = str(num)
    
    for i in range(len(num)):
        if int(num[i]) in n_working:
            break
        elif i == len(num) - 1:
            count = min(count, abs(int(num) - n) + len(num))

print(count)