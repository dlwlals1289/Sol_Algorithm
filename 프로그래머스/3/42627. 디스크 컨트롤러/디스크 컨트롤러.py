import heapq
def solution(jobs):
    answer = 0
    jobs.sort()
    
    current_time = 0
    sum_time = 0
    n = len(jobs)
    
    heap = []
    idx = 0
    while idx < n or heap:
        while idx < n and jobs[idx][0] <= current_time:
            heapq.heappush(heap, [jobs[idx][1], jobs[idx][0]])
            idx += 1
        if heap:
            duration, start = heapq.heappop(heap)
            sum_time += duration + current_time - start
            current_time += duration
        else:
            current_time = jobs[idx][0]
    
    return sum_time // n