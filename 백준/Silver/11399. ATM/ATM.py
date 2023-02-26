# ATM
import copy

n = int(input())

time = list(map(int, input().split()))
time.sort() # 오름차순으로 정렬

sumTime = copy.deepcopy(time) 
result = 0

for i in range(n):
    for j in range(i):
        sumTime[i] += time[j]
    result += sumTime[i]

print(result)