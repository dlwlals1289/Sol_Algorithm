def solution(n, times):
    answer = 1000000000*n
    times.sort()
    
    left, right = 1, times[-1]*n
    
    while left < right:
        mid = (left + right) // 2
    
        tmp = 0
        for time in times:
            tmp += mid // time
        
        if tmp >= n:
            answer = min(answer, mid)
            right = mid
        elif tmp < n :
            left = mid + 1
    
    return answer