# N과 M(1)
import sys

N, M = map(int, sys.stdin.readline().split())
answer = []

def dfs():
    if len(answer) == M:
        print(' '.join(map(str, answer)))
        
    for i in range(1, N+1):
        if i in answer:
            continue
        answer.append(i)
        dfs()
        answer.pop()
          
dfs()