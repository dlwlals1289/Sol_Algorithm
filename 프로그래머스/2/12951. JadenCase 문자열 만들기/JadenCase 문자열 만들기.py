def solution(s):
    answer = ''
    arr = s.split(' ')
    jadencase = []
    
    for i in range(len(arr)):
        if arr[i] == '':
            jadencase.append(arr[i])
        else :
           jadencase.append(arr[i][0].upper()+ arr[i][1:].lower())
    
    answer = ' '.join(jadencase)
    return answer