def solution(numbers):
    answer = []
    
    for x in numbers:
        if x % 2 == 0:
            answer.append(x+1)
        else:
            answer.append(x+1+((x^(x+1)) >> 2))
            
    return answer