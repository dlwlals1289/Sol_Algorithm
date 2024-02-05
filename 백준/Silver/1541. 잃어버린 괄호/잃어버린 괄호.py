# 잃어버린 괄호
import sys
input = sys.stdin.readline

expression = input().split()
expression = expression[0].split('-')

num = []
for i in expression:
    if '+' in i:
        tmp = list(map(int, i.split('+')))
        num.append(sum(tmp))
    else:
        num.append(int(i))

if len(num) == 1:
    print(num[0])
else:
    print(num[0] - sum(num[1:]))