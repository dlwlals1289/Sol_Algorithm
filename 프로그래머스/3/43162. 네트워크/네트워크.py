def solution(n, computers):
    answer = 0
    n = len(computers)
    visited = [False] * n
    
    def dfs(node):
        visited[node] = True
        for i in range(n):
            if computers[node][i] == 1 and not visited[i]:
                dfs(i)
                
    for i in range(n):
        if visited[i] == False:
            dfs(i)
            answer += 1
            
    return answer