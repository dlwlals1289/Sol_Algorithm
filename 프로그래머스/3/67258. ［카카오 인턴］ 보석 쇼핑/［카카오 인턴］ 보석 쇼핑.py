from collections import defaultdict
def solution(gems):
    answer = [0, len(gems)]
    type = set(gems)
    n = len(type)
    cnt = defaultdict(int)
    
    left = 0
    for right, gem in enumerate(gems):
        cnt[gem] += 1
        
        while len(cnt) == n and left <= right:
            if right - left < answer[1] - answer[0]:
                answer[0], answer[1] = left+1, right+1
            cnt[gems[left]] -= 1
            
            if cnt[gems[left]] == 0:
                del cnt[gems[left]]
            left += 1
    return answer