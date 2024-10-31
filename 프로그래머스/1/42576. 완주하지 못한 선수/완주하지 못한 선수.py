def solution(participant, completion):
    answer = ''
    dic = dict()
    
    for i in participant:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    
    for i in completion:
        dic[i] -= 1
    
    for key in dic.keys():
        if dic[key] == 1:
            answer = key
            break
    return answer