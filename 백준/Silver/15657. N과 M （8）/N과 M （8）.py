# N과 M(8)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

num = list(map(int, input().split()))
num.sort()

answer = []
def dfs():
    if len(answer) == M:
        print(' '.join(map(str, answer)))
        return
        
    for i in num:
        if len(answer) > 0 and i < answer[-1]:
            continue
        
        answer.append(i)
        dfs()
        answer.pop()
dfs()