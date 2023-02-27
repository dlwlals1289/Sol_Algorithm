# 쇠막대기
import sys
input = sys.stdin.readline

stick = list(input())
stack = list()
count = 0

for i in range(len(stick)-1):
    if (stick[i] == '('):
        if (stick[i+1] == ')'): # ()
            count += len(stack)
        else :                  # ((
            stack.append(stick[i]) 
    else:       
        if (stick[i+1] == ')'): # ))
            count += 1
            stack.pop()

print(count)