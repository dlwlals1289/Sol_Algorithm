def solution(s):
    answer = 0
    n = len(s)
    stack = []
    dic = {'(' : ')', '[' : ']', '{' : '}'}
    
    for i in range(n):
        stack = []
        flag = True
        for j in range(n):
            now = s[(i+j)%n]
            if now in ['(', '[', '{']:
                stack.append(now)
            elif len(stack) != 0:
                if dic[stack[-1]] == now:
                    stack.pop()
                else :
                    flag = False
                    break
            else:
                flag = False
                break
        
        if flag and len(stack) == 0:
            answer += 1
    return answer