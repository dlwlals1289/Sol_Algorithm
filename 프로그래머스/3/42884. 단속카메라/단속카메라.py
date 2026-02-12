def solution(routes):
    answer = 0
    
    routes.sort(key = lambda x : x[1])
    
    co = -30000
    for route in routes:
        i, o = route
        
        if i > co:
            co = o
            answer += 1
        
    return answer