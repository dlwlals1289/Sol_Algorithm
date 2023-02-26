# 나는야 포켓몬 마스터 이다솜
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

k_dic = dict()
v_dic = dict()
for i in range(1,n+1):
    a = input().rstrip()
    k_dic[i] = a
    v_dic[a] = i

for j in range(m):
    a = input().rstrip()
    if a.isdigit():
        print(k_dic[int(a)])
    else:
        print(v_dic[a])