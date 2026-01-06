def solution(order):
    n = len(order)
    answer = 0
    cur = 0
    scb = []
    
    for i in range(1, n+1):
        scb.append(i)
        
        while scb and scb[-1] == order[cur]:
            scb.pop()
            cur += 1
            answer += 1
    
    return answer