def compareId(x, y):
        for a, b in zip(x, y):
            if a == '*':
                continue
            elif a != b:
                return False
        return True
    
def solution(user_id, banned_id):
    answer = 0
    save = set()
    n = len(user_id)
    m = len(banned_id)
    visited = [False] * n
    
    def dfs(depth, arr):
        if depth == m:
            save.add(tuple(sorted(arr)))
            return
        for i in range(n):
            b_id = banned_id[depth]
            u_id = user_id[i]
            if visited[i] == False and len(b_id) == len(u_id) and compareId(b_id, u_id):
                visited[i] = True
                arr.append(u_id)
                dfs(depth+1, arr)
                visited[i] = False
                arr.pop()
    dfs(0 , [])
    answer = len(save)
    return answer