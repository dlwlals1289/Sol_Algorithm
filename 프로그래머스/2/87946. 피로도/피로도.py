from itertools import permutations
import math

def solution(k, dungeons):
    n = len(dungeons)
    answer = 0
    
    line = [i for i in range(n)]
    
    for i in permutations(line, n):
        tmp = k
        count = 0
        
        for j in i:
            if tmp >= dungeons[j][0]:
                tmp -= dungeons[j][1]
                count += 1
        
        answer = max(answer, count)
    
    return answer