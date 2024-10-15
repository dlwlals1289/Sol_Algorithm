# ABCDE
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
relations = [[] for _ in range(n)]
visited = [False]*(n)
answer = False

for i in range(m):
    x, y = map(int, input().split())
    
    relations[x].append(y)
    relations[y].append(x)

def dfs(now, cnt):
    global answer
    visited[now] = True
    if cnt == 4:
        answer = True
        return
    
    for i in relations[now]: 
        if visited[i] == False:
            dfs(i, cnt + 1)
    visited[now] = False
    
for i in range(n):
    dfs(i,0)
    if answer == True:
        break
    
if answer:
    print(1)
else:
    print(0)