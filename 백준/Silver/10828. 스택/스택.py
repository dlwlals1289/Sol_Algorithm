# 스택
import sys

input=sys.stdin.readline

result = []
n = int(input())

for i in range(0, n):
    str = input().split() 
    if str[0] == "push": # push 일 때 list 맨 끝에 넣기
        result.append(int(str[1]))

    elif str[0] == "pop": # pop 일 때 list 맨 끝 요소 출력 후 삭제
        if len(result)==0:
            print(-1)
        else:
            print(result.pop())

    elif str[0] == "size": # size 일 때 list 길이 출력
        print(len(result))

    elif str[0] == "empty": # list의 길이가 0이면(스택이 비어있으면) "1" 출력
        if len(result) == 0:
            print(1)
        else: 
            print(0)

    elif str[0] == "top": # list의 맨 끝 요소 출력
        if len(result)==0:
            print(-1)
        else:
            print(result[-1])