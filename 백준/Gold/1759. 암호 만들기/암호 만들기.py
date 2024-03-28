# 암호 만들기
import sys
from itertools import combinations
input = sys.stdin.readline

l, c = map(int, input().split())
alphabet = input().split()
alphabet.sort()

for a in combinations(alphabet, l):
    n_a = a.count('a')
    n_i = a.count('i')
    n_u = a.count('u')
    n_e = a.count('e')
    n_o = a.count('o')
    
    sum = n_a + n_i + n_u + n_e + n_o
    
    if 0 < sum < l - 1:
        print(''.join(a))