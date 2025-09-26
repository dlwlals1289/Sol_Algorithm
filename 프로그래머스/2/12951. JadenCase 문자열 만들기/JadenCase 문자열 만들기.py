def solution(s):
    answer = ''
    arr_str = s.split(' ')
    n = len(arr_str)
    
    for i, s in enumerate(arr_str):
        if s != '':
            first, str_tmp = s[0:1], s[1:]
            first = first.upper()
            str_tmp = str_tmp.lower()
            answer += (first + str_tmp)
        
        if i != n-1:
            answer += ' '
    return answer