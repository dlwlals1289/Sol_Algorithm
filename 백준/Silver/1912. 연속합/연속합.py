# 연속합
import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

ans = []
ans.append(array[0])
for i in range(1,n):
    ans.append(max(array[i], ans[i-1]+array[i]))

print(max(ans))