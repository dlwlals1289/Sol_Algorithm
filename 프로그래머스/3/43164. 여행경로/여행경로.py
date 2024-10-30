def solution(tickets):   
    answers = []
    visited = [0 for _ in range(len(tickets))]
    
    def dfs(route):
        if 0 not in visited:
            answers.append([city for city in route])
            return
        for i in range(len(tickets)):
            if visited[i] == 0 and route[-1] == tickets[i][0]:
                visited[i] = 1
                route.append(tickets[i][1])
                dfs(route)
                route.pop()
                visited[i] = 0
                
    for i in range(len(tickets)):
        if tickets[i][0] == "ICN":
            visited[i] = 1
            dfs([tickets[i][0], tickets[i][1]])
            visited[i] = 0

    answers.sort()
    return answers[0]