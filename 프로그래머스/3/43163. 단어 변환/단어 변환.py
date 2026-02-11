from collections import deque

def solution(begin, target, words):
    answer = 0
    len_word = len(begin)
    dist = [0] * (len(words) + 1)
    
    if target not in words:
        return 0
    
    q = deque([])
    q.append((begin, len_word))
    
    while q:
        now, idx = q.popleft()
        
        if now == target:
            return dist[idx]
        for i, word in enumerate(words):
            if dist[i] == 0:
                cnt = 0
                for j, w in enumerate(word):
                    if w == now[j]:
                        cnt += 1
                if cnt == len_word - 1:
                    q.append((word,i))
                    dist[i] = dist[idx] + 1
    return answer