def solution(k, tangerine):
    answer = 0
    dic = {}
    
    for i in range(len(tangerine)):
        if tangerine[i] in dic.keys():
            dic[tangerine[i]] += 1
            continue
        else :
            dic[tangerine[i]] = 1
    
    dic = dict(sorted(dic.items(), key = lambda x : -x[1]))
    
    for i in dic.keys():
        k -= dic[i]
        answer += 1
        
        if k <= 0:
            break
        
    return answer