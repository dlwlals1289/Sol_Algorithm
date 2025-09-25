from collections import defaultdict

def solution(gems):
    n = len(gems)
    answer = [0, n]
    all_gems = len(set(gems))
    counter = defaultdict(int)
    
    left = 0
    for right in range(n):
        counter[gems[right]] += 1
    
        while len(counter) == all_gems:
            if right - left < answer[1] - answer[0]:
                answer = [left+1, right+1]
            
            counter[gems[left]] -= 1
            
            if counter[gems[left]] == 0:
                del(counter[gems[left]])
            left += 1
                
        
    return answer