# 나무 자르기
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tree = list(map(int, input().split()))

start, end = 1, max(tree)

while start <= end:
    mid = (start + end) // 2
    answer = 0
    
    for i in tree:
        if i < mid:
            continue
        answer += (i - mid)
    
    if answer >= M:
        start = mid + 1
    elif answer < M:
        end = mid - 1

print(end)