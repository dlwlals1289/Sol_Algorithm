# 기타 레슨
import sys

n, m = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

start = max(array)
end = sum(array)

answer = end

while(start <= end):
    sum = 0
    count = 1
    mid = (start + end) // 2
 
    for i in array:
        sum += i
        if (sum > mid):
            sum = i
            count += 1
    if count <= m:
        end = mid - 1
        answer = min(mid, answer)
    elif count > m :
        start = mid + 1
        
print(answer)