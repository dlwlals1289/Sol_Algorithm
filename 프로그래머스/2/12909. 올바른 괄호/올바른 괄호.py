def solution(s):
    answer = True
    stack = []
    
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')' and len(stack) != 0 and stack[-1] == '(':
            stack.pop()
        else : 
            return False
    if len(stack) != 0:
        return False
    return True