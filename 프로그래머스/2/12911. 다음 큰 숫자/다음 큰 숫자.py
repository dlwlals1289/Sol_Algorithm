def solution(n):
    answer = 0
    cntOne = bin(n)[2:].count('1')
    
    while True:
        n += 1
        if bin(n)[2:].count('1') == cntOne:
            answer = n
            break
    return answer