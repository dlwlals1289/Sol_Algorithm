def solution(brown, yellow):
    answer = [0, 0]
    
    for i in range(1, yellow+1):
        if yellow % i == 0: # 노란색 타일 개수의 약수
            row = yellow // i
            col = yellow // row
            
            if 2 * (row + col + 2) == brown:
                answer[0] = col + 2;
                answer[1] = row + 2;
    return answer