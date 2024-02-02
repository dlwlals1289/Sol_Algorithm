# 패션왕 신해빈

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    clothes = dict()
    
    for i in range(N):
        cloth, sort = input().split()
        
        if sort in clothes.keys():
            clothes[sort] += 1

        else:
            clothes[sort] = 1
    
    answer = 1
    
    for cnt in clothes.values():
        answer *= (cnt + 1)
    
    print(answer - 1)
    
    