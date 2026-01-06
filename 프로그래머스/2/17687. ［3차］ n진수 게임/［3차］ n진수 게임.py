def trans(num, n):
    tmp = []
    
    while num > 0:
        remainder = num % n
        if remainder > 9:
            remainder = hex(remainder)[2].upper()
        tmp.append(str(remainder))
        num //= n
    
    return ''.join(reversed(tmp))

def solution(n, t, m, p):
    answer = ''
    strAns = '0'
    
    num = 1
    while len(strAns) < (m * t):
        strAns += trans(num, n)
        num +=1

    for i in range(p-1, m*t, m):
        answer += strAns[i]
        
        if len(answer) == t:
            break
    return answer