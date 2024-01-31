# N과 M(5)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

num = list(map(int, input().split()))
num.sort()

answer = []
def dfs():
    if len(answer) == M:
        print(' '.join(map(str, answer)))
    for i in num:
        if i in answer:
            continue
        answer.append(i)
        dfs()
        answer.pop()

dfs()