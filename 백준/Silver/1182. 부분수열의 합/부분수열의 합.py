# 부분수열의 합
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8) #재귀 리미트

n, s = map(int, input().split())
num= list(map(int, input().split()))
ans = []
count = 0

def dfs(a):
    global count
    if sum(ans) == s and len(ans)>0:
        count += 1
    
    for i in range(a, n):
        ans.append(num[i])
        dfs(i+1)
        ans.pop()

dfs(0)
print(count)