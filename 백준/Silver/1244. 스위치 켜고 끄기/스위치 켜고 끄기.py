# 스위치 끄고 켜기

import sys

N = int(input())
switch = list(map(int, input().split()))
switch.insert(0, 0)

M = int(input())

for _ in range(M):
    sex, number = map(int, input().split())
    
    if(sex == 1):   # 학생이 남자일 경우 
        index = number
        while (index < N+1):
            if (switch[index] == 1):
                switch[index] = 0
            else:
                switch[index] = 1
            
            index += number

    else:           # 학생이 여자일 경우
        maxGap = min(number - 1, (N - number))
        index = number
        for i in range(1, maxGap+1):
            if(switch[index - i] == switch[index + i]):
                if switch[index - i] == 0 :
                    switch[index - i] = 1
                    switch[index + i] = 1
                else:
                    switch[index - i] = 0
                    switch[index + i] = 0
            else:
                break
        if (switch[number] == 1):
            switch[number] = 0
        else:
            switch[number] = 1

for k in range(1, N+1):
    print(switch[k], end=" ")
    if k % 20 == 0:
        print()