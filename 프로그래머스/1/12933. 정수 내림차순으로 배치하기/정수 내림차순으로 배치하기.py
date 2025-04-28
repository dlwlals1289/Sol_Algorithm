def solution(n):
    answer = 0
    
    arr= list(str(n))
    arr.sort(reverse= True)
    return int(''.join(arr))