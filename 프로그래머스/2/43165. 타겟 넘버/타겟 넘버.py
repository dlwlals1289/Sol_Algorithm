from itertools import combinations
def solution(numbers, target):
    answer = 0
    
    for i in range(1, len(numbers)+1):
        for j in combinations(range(len(numbers)), i):
            tmp = 0
            
            for k in range(len(numbers)):
                if k in j:
                    tmp += numbers[k]
                else:
                    tmp -= numbers[k]
            if tmp == target:
                answer += 1
    
    return answer