
def solution(citations):
    answer = 0
    n = len(citations)
    
    citations.sort()
    
    for h in range(1, 10001):
        for idx, num in enumerate(citations):
            if h <= num and n-idx >= h:
                answer = max(answer, h)
                              
    return answer