#15:01
def solution(stones, k):
    answer = 200000000
    n = len(stones)
    left, right = 1, answer
    
    def calc(person):
        tmp = 0
        for s in stones:
            if s - person < 0:
                tmp += 1
                if tmp == k:
                    return False
            else:
                tmp = 0
        return True
    
    while left <= right:
        mid = (left + right) // 2
        
        if calc(mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    return answer