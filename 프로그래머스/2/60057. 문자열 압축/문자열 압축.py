def solution(s):
    answer = len(s)
    n = len(s) // 2
    m = len(s)
    
    for i in range(1, n+1):
        cnt = 1
        now = s[0:i]
        save = ''
        idx = i
        
        while idx < m:
            if s[idx: idx+i] == now:
                cnt += 1
            else:
                if cnt == 1:
                    save += now
                else :
                    save += str(cnt)+now
                now = s[idx: idx+i]
                cnt = 1
            idx = idx+i
        if cnt == 1:
            save += now
        else :
            save += str(cnt)+now
        answer = min(answer, len(save))
            
        
    return answer