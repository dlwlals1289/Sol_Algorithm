from collections import deque

def solution(x, y, n):
    answer = 0
    dp = [0] * (y+1)
    visited = deque([x])
    
    while visited:
        now = visited.popleft()
        
        if now == y:
            return dp[y]
        if now*2 <= y and dp[now*2] == 0:
            dp[now*2] = dp[now] + 1
            visited.append(now*2)
            
        if now*3 <= y and dp[now*3] == 0:
            dp[now*3] = dp[now] + 1
            visited.append(now*3)
            
        if now + n <= y and dp[now+n] == 0:
            dp[now+n] = dp[now] + 1
            visited.append(now+n)
    return -1