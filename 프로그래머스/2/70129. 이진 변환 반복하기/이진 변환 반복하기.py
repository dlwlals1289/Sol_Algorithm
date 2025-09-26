def solution(s):
    answer = [0, 0]
    
    while s != '1':
        arr = list(s)
        one = 0
        
        for i in arr:
            if i == '0':
                answer[1] += 1
            else:
                one += 1
        
        s = bin(one)[2:]
        answer[0] += 1
        
    return answer