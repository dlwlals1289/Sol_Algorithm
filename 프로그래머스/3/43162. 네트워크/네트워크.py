def solution(n, computers):
    answer = 0
    
    visited = [False] * n
              
    def dfs(x):
        for i in range(n):
            if i != x and visited[i] != True and computers[x][i] == 1:
                visited[i] = True
                dfs(i)
    
    for i in range(n):
        if visited[i] == False:
            dfs(i)
            answer += 1
            
            
    return answer