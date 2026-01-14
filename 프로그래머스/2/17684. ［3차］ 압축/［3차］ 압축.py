def solution(msg):
    answer = []
    n = len(msg)
    dic = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    idx = 0
    w, c = '', ''
    while idx < n:
        w += msg[idx]
        
        if idx == n-1:
            answer.append(dic.index(w))
            break
        
        c = msg[idx+1]
        if w+c in dic:
            idx += 1
            continue
        dic.append(w+c)
        answer.append(dic.index(w))
        idx += 1
        w = ''
    return answer