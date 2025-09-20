import math

def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    idx = 0
    
    while idx < n:
        count = 0
        diff = 100 - progresses[idx]
        days = math.ceil(diff / speeds[idx])
        
        for i in range(idx, n):
            progresses[i] += (days * speeds[i])
        
        for i in range(idx, n):
            if progresses[i] >= 100:
                idx += 1
                count += 1
            else :
                break;
        answer.append(count)
        
    return answer