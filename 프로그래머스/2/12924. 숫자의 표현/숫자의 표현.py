def solution(n):
    answer = 0
    
    for i in range(1, n+1):
        idx = i
        sum = 0
        
        while sum < n:
            sum += (idx)
            idx += 1
        
        if sum == n:
            answer += 1
    return answer