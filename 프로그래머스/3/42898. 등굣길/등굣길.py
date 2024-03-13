def solution(m, n, puddles):
    answer = 0
    
    route = [[0]*(m+1) for _ in range(n+1)]
    route[1][1] = 1
    
    for a,b in puddles:
        
        route[b][a] = -1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            elif route[i][j] == -1:
                continue
            elif route[i-1][j] == -1:
                route[i][j] = route[i][j-1]
            elif route[i][j-1] == -1:
                route[i][j] = route[i-1][j]
            else:
                route[i][j] = route[i-1][j] + route[i][j-1]
    answer = (route[n][m]) % 1000000007
    return answer