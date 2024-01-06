#요세푸스 문제0

import sys

N, K = map(int, input().split())

index = K
array = []
r_array = []

for i in range(1,N+1):
    array.append(i)

r_array.append(array.pop(index-1))

for i in range(1,N):
    index = index + K - 1
    
    while (index > len(array)):
        index -= len(array)
        
    r_array.append(array.pop(index-1))
        
print("<", end="")
print(", ".join(map(str, r_array)), end="")
print(">")