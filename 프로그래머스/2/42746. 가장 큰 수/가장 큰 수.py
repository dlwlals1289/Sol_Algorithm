def solution(numbers):
    answer = ''
    
    arr = []
    for i in numbers:
        arr.append(str(i))
    
    arr.sort(key = lambda x : (x*4)[:4], reverse = True)
    
    answer = "".join(arr)
    
    if "0"*len(arr) == answer:
        answer = "0"
    
    return answer