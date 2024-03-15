def solution(n, computers):
    answer = 0
    
    network = [[] for _ in range(n)]
    visited = []
    
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                network[i].append(j)
                
    def dfs(a):
        for node in network[a]:
            if node not in visited:
                visited.append(node)
                dfs(node)
    
    for i in range(n):
        if i not in visited:
            visited.append(i)
            answer += 1
            dfs(i)
    
    return answer