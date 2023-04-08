# 파도반 수열

import sys
input = sys.stdin.readline

triangle = [1,1,1,2,2]

T = int(input())

for i in range(T):
    a = int(input())
    
    l_tri = len(triangle)
    if l_tri < a : 
        for j in range(l_tri, a):
            triangle.append(triangle[j-1] + triangle[j-5])
    
    print(triangle[a-1])