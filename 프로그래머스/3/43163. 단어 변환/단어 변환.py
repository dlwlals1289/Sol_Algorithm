from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0
    
    q = deque()
    q.append((begin, 0))
    
    while q:
        visited = [0 for _ in range(len(words))]
        tmp, idx = q.popleft()
        if tmp == target:
            break
        for i in range(len(words)):
            for j in range(len(words[i])):
                if words[i][j] == tmp[j]:
                    visited[i] += 1
        for i in range(len(visited)):
            if visited[i] == len(target) - 1:
                q.append((words[i], idx+1))
                # words[k] = str(idx)
                
    return idx