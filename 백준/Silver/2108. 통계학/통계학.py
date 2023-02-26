# 통계학
from collections import Counter
import sys

n = int(sys.stdin.readline())
num = []
sum = 0 # 평균을 위함
for i in range(n):
    a = int(sys.stdin.readline())
    num.append(a)
    sum += a

# 산술평균 
mean = sum / n
print(round(mean))

# 중앙값
num.sort()
median = num[round(n//2)]
print(median)

# 최빈값
count = Counter(num).most_common()
if n == 1:
    print(num[0])
elif count[0][1] == count[1][1]:
    print(count[1][0])
else:
    print(count[0][0])


# 범위
range = num[-1] - num[0]
print(range)
