# N과 M(4)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
answer = []

def dfs():
    if len(answer) == M :
        print(' '.join(map(str, answer)))
        return
    
    for i in range(1, N+1):
        if len(answer) > 0 and answer[-1] > i:
            continue
        
        answer.append(i)
        dfs()
        answer.pop()

dfs()