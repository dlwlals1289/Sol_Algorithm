import math
def solution(n,a,b):
    answer = 0
    
    idx = 1
    a, b = a-1, b-1
    while True:
        div = int(math.pow(2,idx))
        
        if((a//div) == (b//div)):
            answer = idx
            break
        else :
            idx += 1
    

    return answer