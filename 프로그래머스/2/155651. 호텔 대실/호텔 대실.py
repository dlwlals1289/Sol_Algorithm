import heapq
def to_minutes(time):
    hour, minute = map(int, time.split(':'))
    
    return hour*60 + minute
    
def solution(book_time):
    answer = 0
    n = len(book_time)
    book_time.sort(key=lambda x : x[0])
    hq = []
    
    for i in book_time:
        if hq and hq[0] <= to_minutes(i[0]):
            heapq.heappop(hq)
        heapq.heappush(hq, to_minutes(i[1])+10)
    return len(hq)