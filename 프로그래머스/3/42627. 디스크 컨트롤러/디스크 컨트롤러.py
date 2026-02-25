from heapq import heappush, heappop
from collections import deque
def solution(jobs):
    answer = 0
    n = len(jobs)
    jobs.sort()
    hq = []

    time = 0
    idx = 0
    
    while idx < n or hq:
        while idx < n and jobs[idx][0] <= time:
            entered, dur = jobs[idx]
            heappush(hq, [dur, entered])
            idx += 1
        
        if hq :
            dur, entered  = heappop(hq)
            time += dur
            answer += (time - entered)
        else:
            time = jobs[idx][0]
    
    return answer // n