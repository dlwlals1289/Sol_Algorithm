def solution(numbers):
    answer = -1
    nums = [0,1,2,3,4,5,6,7,8,9]
    
    arr = (set(nums) - set(numbers))
    answer = sum(arr)
    return answer