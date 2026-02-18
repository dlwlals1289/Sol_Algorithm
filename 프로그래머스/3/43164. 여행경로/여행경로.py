from collections import deque
def solution(tickets):
    answer = []
    n = len(tickets)
    visited = [False] * n
    
    def dfs(route):
        if len(route) == n + 1:
            if answer and answer[0] > route:
                answer.clear()
                answer.append(route)
                return
            answer.append(route)
            return
            
        
        for idx, ticket in enumerate(tickets):
            if not visited[idx] and route[-1] == ticket[0]:
                visited[idx] = True
                dfs(route+[ticket[1]])
                visited[idx] = False
        
    
    for idx, ticket in enumerate(tickets):
        depart, dest = ticket
        
        if depart == 'ICN':
            visited[idx] = True
            dfs(ticket)
            visited[idx] = False
    
    return answer[0]