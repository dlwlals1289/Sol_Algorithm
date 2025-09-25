def solution(tickets):
    answer = []
    n = len(tickets)
    used = [False] * n
    
    def dfs(route):
        if len(route) == n+1:
            answer.append(route[:])
        for i, t in enumerate(tickets):
            if not used[i] and route[-1] == t[0]:
                used[i] = True
                route.append(t[1])
                dfs(route)
                used[i] = False
                route.pop()
    
    for i, ticket in enumerate(tickets):
        if ticket[0] == "ICN":
            used[i] = True
            dfs([ticket[0], ticket[1]])
            used[i] = False
    answer.sort()
    return answer[0]
