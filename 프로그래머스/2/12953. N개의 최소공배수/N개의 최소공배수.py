def solution(arr):
    def getGCD(a, b):
        for i in range(b, a*b+1):
            if i % a == 0 and i % b == 0:
                return i
        return 1
    arr.sort()
    answer = getGCD(arr[0], arr[1])
    
    for i in range(2, len(arr)):
        answer = getGCD(answer, arr[i])
    
    return answer  