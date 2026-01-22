def solution(storey):
    answer = 0
    
    while storey > 0:
        tmp = storey % 10
        
        if tmp > 5:
            answer += (10 - tmp)
            storey += (10 - tmp)
        elif tmp < 5:
            answer += tmp
        else :
            if (storey % 100) // 10 >= 5:
                answer += (10 - tmp)
                storey += (10 - tmp)
            else:
                answer += tmp
        storey //= 10

    return answer