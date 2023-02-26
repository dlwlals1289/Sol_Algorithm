# 수 정렬하기 2

import sys
        
n = int(input())

merge = list() # 데이터 넣을 리스트 생성

for i in range(n):
    merge.append(int(sys.stdin.readline())) # 매 줄마다 입력 받아 바로 리스트에 넣기

merge.sort()

for i in merge:
    print(i)