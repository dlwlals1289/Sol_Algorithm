from collections import deque
def solution(begin, target, words):
    answer = 0
    n = len(words)
    m = len(words[0])
    if target not in words:
        return 0
    
    q = deque()
    q.append((begin, 0))
    
    visited = []
    visited.append(begin)
    
    while q:
        now, cnt = q.popleft()
        
        if now == target:
            answer = cnt
            break
        
        for word in range(n):
            if words[word] not in q and words[word] not in visited:
                count = 0
                for idx in range(m):
                    if now[idx] == words[word][idx]:
                        count += 1
                
                if count == m-1:
                    q.append((words[word], cnt+1))
                    visited.append(words[word])
        answer = cnt
    
    return answer