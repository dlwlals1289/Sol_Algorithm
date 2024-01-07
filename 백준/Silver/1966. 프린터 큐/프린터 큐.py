# 프린트 큐
import sys
from collections import deque

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    
    importance = list(map(int, input().split()))
    array = deque()
    answer = []
    for j in range(N):
        array.append((j,importance[j]))
    
    importance.sort(key=lambda x:-x)
    
    for j in range(N):
        while(importance[j] != array[0][1]):
            array.append(array.popleft())
        answer.append(array.popleft()[0])
    
    for j in range(N):
        if (answer[j] == M):
            print(j+1)
            break
