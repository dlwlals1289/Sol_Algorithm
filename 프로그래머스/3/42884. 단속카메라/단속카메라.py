def solution(routes):
    answer = 1
    
    routes.sort(key = lambda x : x[0])
    
    last_end = routes[0][1]
    
    for start, end in routes:
        if last_end < start:
            last_end = end
            answer += 1
        elif end < last_end:
            last_end = end
            
    return answer