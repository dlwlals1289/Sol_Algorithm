# 생태학
import sys
input = sys.stdin.readline

dic = dict()
total = 0

while True:
    a = input().rstrip()
    # print(a)
    if not a:
        break
    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1
    total += 1

dic2 = dict(sorted(dic.items()))

for i in dic2:
    # print(f'{dic2}')
    a = dic[i]
    a = (a/total)*100
    print("%s %.4f" %(i, a))

