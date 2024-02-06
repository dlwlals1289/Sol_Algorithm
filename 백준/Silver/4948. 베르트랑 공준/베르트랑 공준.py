# 베르트랑 공준
import sys
input = sys.stdin.readline
max_num = (123457)*2 +1

arr = [1 for _ in range(max_num)]
arr[0] = 0

for i in range(2, int(max_num**(1/2))):
    if arr[i] == 0:
        continue
    for j in range(i*i, max_num, i):
        arr[j] = 0

state = True
while state:
    n = int(input())
    
    if n == 0:
        state = False
        continue
    
    print(sum(arr[n+1:2*n+1]))
        