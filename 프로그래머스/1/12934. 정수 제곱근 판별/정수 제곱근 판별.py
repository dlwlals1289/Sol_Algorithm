import math
def solution(n):
    answer = 0
    
    tmp = math.sqrt(n) 
    
    if(tmp % 1 == 0):
        answer = math.pow(tmp+1, 2)
    else:
        answer = -1
    return answer