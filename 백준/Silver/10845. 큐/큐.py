# queue
import sys
input=sys.stdin.readline

n = int(input())

queue = []
for i in range(n):
    command = input().split()
    if command[0] == "push": # push 일 때
        queue.append(command[1])
    elif command[0] == "pop": # pop 일 때
        if(len(queue)==0):
            print(-1)
        else:
            print(queue.pop(0))
    elif command[0] == "size": # size 일 때
        print(len(queue))
    elif command[0] == "empty": # empty 일 때
        if(len(queue)==0):
            print(1)
        else:
            print(0)
    elif command[0] == "front": # front 일 때
        if(len(queue)==0):
            print(-1)
        else:
            print(queue[0])
    elif command[0] == "back": # back 일 때
        if(len(queue)==0):
            print(-1)
        else:
            print(queue[-1])