from heapq import heappush, heappop, heapify
def solution(n, works):
    answer = 0
    arr = []
    
    for work in works:
        heappush(arr, -work)
    
    for i in range(n):
        w = heappop(arr)
        
        if w+1 < 0:
            heappush(arr, w+1)
        else :
            heappush(arr, 0)
        
    
    for num in arr:
        answer += ((-num)**2)
    
    return answer