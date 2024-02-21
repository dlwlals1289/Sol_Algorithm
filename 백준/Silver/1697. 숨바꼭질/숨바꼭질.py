# 숨바꼭질
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
visited = [0] * 100001

def bfs():
    que = deque()
    que.append(n)
    
    while len(que)>0:
        v = que.popleft()
        
        if v == k:
            print(visited[v])
            break
        
        for i in (v-1, v+1, v*2):
            if 0 <= i <= 100000 and visited[i] == 0:
                visited[i] = visited[v] + 1
                que.append(i)

bfs()