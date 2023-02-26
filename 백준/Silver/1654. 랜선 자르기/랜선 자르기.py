# 랜선 자르기

import sys

k, n = map(int, input().split())

length = []
answer = 0

for i in range(k):
    length.append(int(input()))

start = 1
end = max(length)

while(start <= end):
# for i in range(2):
    count = 0
    mid = int((start + end) / 2)
    
    for i in length:
        a = i 
        a //= mid
        count += a

    if count >= n:
        answer = mid
        start = mid + 1
    elif count < n:
        end = mid - 1

print(answer)