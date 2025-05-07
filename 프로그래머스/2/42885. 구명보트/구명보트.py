def solution(people, limit):
    answer = 0
    idx = 0
    num = len(people)
    visited = [False for _ in range(num)]
    
    people.sort()
   
    for i in range(num-1, -1, -1):
        if visited[i] == True :
            continue
        elif people[i] + people[idx] <= limit:
            visited[i] = True
            visited[idx] = True
            answer += 1
            idx += 1
        else :
            visited[i] = True
            answer += 1
            
    return answer