from collections import deque
def solution(begin, target, words):
    answer = 0
    n = len(words)
    m = len(words[0])
    
    if target not in words:
        return 0
    
    q = deque([(begin, 0)])
    
    visited = set([begin])
    
    while q:
        now, cnt = q.popleft()
        
        if now == target:
            answer = cnt
        
        for word in words:
            if word not in visited:
                
                diff = sum(1 for a, b in zip(now, word) if a != b)
                
                if diff == 1:
                    q.append((word, cnt+1))
                    visited.add(word)
    
    return answer