# Z
import sys 
input = sys.stdin.readline

N, r, c = map(int, input().split())

tmp = 2**(N-1)
tmp_r = 2**(N-1)
tmp_c = 2**(N-1)
answer = 0 

while (tmp >= 1):
    index = 0
        
    if r >= tmp_r:
        index += 2
        tmp_r = tmp_r + (tmp//2)
        if c >= tmp_c:
            index += 1
            tmp_c = tmp_c + (tmp//2) # index = 3
        else:
            tmp_c = tmp_c - (tmp//2) # index = 2
    else:
        tmp_r = tmp_r - (tmp//2)
        if c >= tmp_c:
            index += 1
            tmp_c = tmp_c + (tmp//2) # index = 1
        else:
            tmp_c = tmp_c - (tmp//2) # index = 0
    
    answer += 4**(N-1) * index
    N -= 1
    tmp //= 2 

print(answer)