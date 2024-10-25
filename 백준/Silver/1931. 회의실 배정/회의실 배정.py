# 회의실배정 
import sys
input = sys.stdin.readline

n = int(input())
time = [list(map(int, input().split())) for _ in range(n)]
time.sort(key= lambda x : (x[1], x[0]))
answer = 1

end = time[0][1]
for i in range(1, n):
    if end <= time[i][0]:
        answer += 1
        end = time[i][1]

print(answer)