# 숫자카드 2

import sys
from bisect import bisect_left, bisect_right

def find(array, x):
    right = bisect_right(array,x)
    left = bisect_left(array, x)
    return right - left

n = int(input())
n_array = list(map(int, sys.stdin.readline().split()))

m = int(input())
m_array = list(map(int, sys.stdin.readline().split()))

n_array.sort() # 순차적으로 정렬

answer = []
for i in m_array:
    answer.append(find(n_array, i))

print(*answer)

