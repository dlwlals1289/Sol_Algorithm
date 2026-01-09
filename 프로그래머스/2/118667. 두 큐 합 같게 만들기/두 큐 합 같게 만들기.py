from collections import deque

def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    total  = sum1 + sum2
    limit = (len(q1) + len(q2)) * 3
    
    
    if total % 2 == 1:
        return -1
    
    while answer < limit :
        if not q1 or not q2:
            return -1
        
        if sum1 == sum2 :
            return answer
        
        if sum1 > sum2:
            tmp = q1.popleft()
            q2.append(tmp)
            sum2 += tmp
            sum1 -= tmp
        elif sum2 > sum1:
            tmp = q2.popleft()
            q1.append(tmp)
            sum1 += tmp
            sum2 -= tmp
        
        answer += 1
    return -1