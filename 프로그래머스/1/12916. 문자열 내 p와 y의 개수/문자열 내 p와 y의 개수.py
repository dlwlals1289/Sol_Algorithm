def solution(s):
    answer = True
    cntP = 0
    cntY = 0
    
    for c in s:
        tmp = c.upper()
        if tmp == 'P':
            cntP += 1
        elif tmp == 'Y':
            cntY += 1
    
    if cntP == cntY :
        return True

    return False