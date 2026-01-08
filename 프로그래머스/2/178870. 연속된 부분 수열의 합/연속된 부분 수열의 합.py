def solution(sequence, k):
    answer = [0, len(sequence)]
    start, end = 0, 0
    sum = 0
    
    for idx, num in enumerate(sequence):    
        sum += num
        end = idx
        
        while sum > k:
            sum -= sequence[start]
            start += 1
        
        if sum == k and answer[1] - answer[0] > end - start:
            answer[0], answer[1] = start, end
            # print(answer)
                      
    return answer