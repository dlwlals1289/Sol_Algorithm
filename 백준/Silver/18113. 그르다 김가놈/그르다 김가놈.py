#그르다 김가놈
import sys

n, k, m = map(int, sys.stdin.readline().split()) 
array = list(int(sys.stdin.readline()) for _ in range(n))
k_list = []
p = -1

for i in range(n):
    if array[i] >= 2*k:
        k_list.append(array[i] - 2*k)
    elif array[i] < 2*k and array[i] >= k:
        k_list.append(array[i] - k)

start = 1
end = max(array)

while(start <= end):
    count = 0
    mid = (start + end) // 2
    
    for i in k_list:
        count += (i//mid)
    
    if count >= m:
        p = max(p, mid)
        start = mid + 1
    else:
        end = mid - 1

print(p)