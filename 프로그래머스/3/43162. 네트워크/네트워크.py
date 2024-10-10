import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
            
def solution(n, computers):
    answer = 0
    networks = [[] for _ in range(n)]
    visited = []
    
    def dfs(a):
        for i in networks[a]:
            if i not in visited:
                visited.append(i)
                dfs(i)
    
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                networks[i].append(j)
                
    for i in range(n):
        if i not in visited:
            visited.append(i)
            dfs(i)
            answer += 1

    return answer