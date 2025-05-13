def solution(want, number, discount):
    answer = 0
    n = len(discount)
    m = len(want)
    
    for i in range(n):
        tmp = 0
        for j in range(m):
            if discount[i:i+10].count(want[j]) == number[j]:
                tmp += 1
        
        if tmp == m:
            answer += 1
            
    return answer