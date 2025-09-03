def solution(numbers, target):
    answer = 0
    n = len(numbers)
    
    def dfs(depth, sum):
        nonlocal answer
        if depth == n:
            if sum == target:
                answer += 1
            return 

        dfs(depth+1, sum+numbers[depth])
        dfs(depth+1, sum-numbers[depth])
        
        
    dfs(0, 0)
    return answer