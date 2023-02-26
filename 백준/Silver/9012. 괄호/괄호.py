# 괄호

n = int(input())

for i in range(n):
    str = input() # string list에 한 글자씩 넣기
    parenthesis = 0

    for j in range(len(str)): # '('와 ')'의 개수 파악하기
        if parenthesis == -1:
            break
        else:
            if str[j] == '(':
                parenthesis += 1
            elif str[j] == ')':
                parenthesis -= 1
    
    if parenthesis != 0: # 괄호의 짝이 안 맞으면
        print("NO")
    else:
        print("YES")