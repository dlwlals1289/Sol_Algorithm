# 좌표압축

import sys
input = sys.stdin.readline

n = int(input())

array = list(map(int, input().split()))

answer = sorted(set(array))

dic = {answer[i] : i for i in range(len(answer))}

for i in array:
    print(dic[i], end = ' ')