def solution(A, B):
    answer = 0
    n = len(A)
    
    A.sort()
    B.sort()
    
    visited = [False] * n
    idx = 0
    for i in range(n):
        for j in range(idx, n):
            if A[i] < B[j]:
                idx = j + 1
                answer += 1
                break
    return answer