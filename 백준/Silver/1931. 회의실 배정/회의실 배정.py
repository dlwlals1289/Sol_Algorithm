import sys

n = int(input())
schedule = []
answer = [[0,0]]

for i in range(n):
    schedule.append(list(map(int, input().split())))

schedule.sort(key = lambda x:(x[1] ,x[0])) # 끝나는 시간 기준 오름차순 정렬 한 후 시작하는 시간도 오름차순 정렬

for i in schedule:
    start = answer[-1][0]
    end = answer[-1][1]
    
    if end <= i[0]:
        answer.append(i)
print(len(answer)-1)