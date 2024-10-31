def solution(nums):
    answer = 0
    n = len(nums)
    
    answer = min(n//2, len(set(nums)))
    return answer