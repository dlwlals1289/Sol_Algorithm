from heapq import heappop, heappush

def solution(n, works):
    answer = 0
    hq = []
    
    for work in works:
        heappush(hq, -work)
    
    for i in range(n):
        work = heappop(hq)
        
        heappush(hq, min(work + 1,0))
    
    for num in hq:
        answer += (num*num)
    return answer