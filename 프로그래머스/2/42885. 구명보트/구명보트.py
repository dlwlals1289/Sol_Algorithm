def solution(people, limit):
    n = len(people)
    answer = 0
    visited = [False] * n
    
    people.sort()
    left, right = 0, n-1
    
    while left <= right:
        if people[left] + people[right] <= limit:
            answer += 1
            left += 1
            right -= 1
        else:
            answer += 1
            right -= 1
    return answer