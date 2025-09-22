from itertools import permutations

def solution(numbers):
    answer = 0
    n = len(numbers)
    arr = list(numbers)
    
    result = set()
    for i in range(1, n+1):
        for p in permutations(arr, i):
            result.add(int("".join(p)))
    
    
    for i in result:
        flag = True
        
        if i == 0 or i == 1:
            continue
            
        for j in range(2, i):
            if i % j == 0:
                flag = False
                break
        
        if flag == True:
            answer += 1
    return answer