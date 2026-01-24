from collections import Counter

def solution(weights):
    answer = 0
    cnt = Counter(weights)
    
    for w, c in cnt.items():
        answer += (c * (c - 1) // 2)
         
        tmp = (w * 3) / 2
        if tmp in cnt and w < tmp:
            answer += c * cnt[tmp]
            
        tmp = w * 2
        if tmp in cnt and w < tmp:
            answer += c * cnt[tmp]
        
        tmp = (w * 4) / 3
        if tmp in cnt and w < tmp:
            answer += c * cnt[tmp]
    
    return answer