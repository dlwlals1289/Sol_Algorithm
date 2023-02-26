# 국영수
import sys

n = int(input())


students = list()

for i in range(n):
    p = {"name" : "", "kor" : 0, "eng" : 0, "math" : 0}
    p['name'], p['kor'], p['eng'], p['math'] = sys.stdin.readline().split()
    students.append([p['name'], int(p['kor']), int(p['eng']), int(p['math'])])

students.sort(key = lambda x : (-x[1] , x[2],-x[3],x[0]))

for i in students:
    print(i[0])