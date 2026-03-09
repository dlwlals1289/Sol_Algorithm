# 문자열 잘라내기
import sys
input = sys.stdin.readline

r, c = map(int, input().split())

arr = [[] for _ in range(c)]
for i in range(r):
    str = input().rstrip()
    
    for j in range(c):
        arr[j].append(str[j])

left, right = 0, r
answer = 0
while left < right:
    mid = ( left + right ) // 2
    
    s = set()
    
    for i in range(c):
        s.add(''.join(arr[i][mid:r]))
    
    if len(s) < c:
        right = mid
        continue
    answer = mid
    left = mid + 1
print(answer)