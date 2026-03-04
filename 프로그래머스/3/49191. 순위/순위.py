from collections import deque
def solution(n, results):
    answer = 0
    graph = [[] for _ in range(n+1)]
    win_cnt = [0]*(n+1)
    lose_cnt = [0] * (n+1)
    
    for result in results:
        a, b = result
        graph[a].append(b)
        
    for i in range(1, n+1):
        q = deque([i])
        visited = [False] * (n+1)
        visited[i] = True
        cnt = 0

        while q:
            now = q.popleft()
            
            for nx in graph[now]:
                if not visited[nx]:
                    q.append(nx)
                    cnt += 1
                    lose_cnt[nx] += 1
                    visited[nx] = True
        win_cnt[i] = cnt
    
    for i in range(1, n+1):
        if win_cnt[i] + lose_cnt[i] == n-1:
            answer += 1
    return answer