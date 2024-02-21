# 숨바꼭질3
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
visited = [-1]*100001

def bfs():
    que = deque()
    que.append(n)
    visited[n] = 0
    
    while len(que)>0:
        v = que.popleft()
        
        if v == k:
            print(visited[v])
            break
        
        for i in (v-1, v+1, v*2):
            if 0 <= i <= 100000 and visited[i] == -1:
                if i == v*2:
                    visited[i] = visited[v]
                    que.appendleft(i)
                else:
                    visited[i] = visited[v] + 1
                    que.append(i)

bfs()