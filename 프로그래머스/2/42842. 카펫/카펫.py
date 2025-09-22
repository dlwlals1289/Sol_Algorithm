def solution(brown, yellow):
    answer = []
    
    for row in range(1, ((yellow+1)//2)+1):
        if yellow % row == 0:
            col = (yellow // row)
            
            tmp = 2 * (col + row + 2)
            
            if tmp == brown:
                answer.append(col+2)
                answer.append(row+2)
                break
            
    return answer