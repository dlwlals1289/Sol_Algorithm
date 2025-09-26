def solution(n, times):
    left, right = 1, max(times) * n
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        total = 0

        for time in times:
            total += (mid // time)
        
        if total < n:
            left = mid + 1
        else:
            right = mid - 1
            answer = mid
    
    return answer