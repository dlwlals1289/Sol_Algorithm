def solution(stones, k):
    answer = 0
    n = len(stones)
    
    left, right = min(stones), max(stones)
    
    while left <= right:
        mid = (left + right)//2
        cnt = 0
        
        for stone in stones:
            if stone < mid:
                cnt += 1
                
                if cnt == k:
                    break
            else:
                cnt = 0
        if cnt >= k:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1
            
    return answer