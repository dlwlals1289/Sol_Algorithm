from collections import deque

def solution(prices):
    n = len(prices)
    answer = [0] * n
    
    for i in range(n):
        time = 0
        for j in range(i+1, n):
            if prices[i] <= prices[j]:
                time += 1
            else:
                time += 1
                break
        answer[i] = time
        
        
    return answer