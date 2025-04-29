def solution(A,B):
    answer = 0
    l = len(A)
    A.sort()
    B.sort()
    for i in range(l):
        answer += (A[i] * B[l - i -1])

    return answer