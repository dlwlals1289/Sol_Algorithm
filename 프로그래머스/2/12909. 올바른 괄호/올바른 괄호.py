def solution(s):
    answer = True
    stack = []
    
    for str in s:
        if str == '(':
            stack.append(str)
            continue
        if len(stack) > 0:
            tmp = stack.pop()
        
            if tmp != '(':
                return False
        else:
            answer = False
    if len(stack) != 0:
        return False
    return answer