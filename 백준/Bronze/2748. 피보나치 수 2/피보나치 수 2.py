# 피보나치 수 2

import sys

n = int(input())

d = [0 for i in range(n+1)]
d[1] = 1

def fibonaci(i):
    if i == 0:
        return 0
    if i == 1 :
        return d[i]
    else:
        if d[i-1] == 0:
            d[i-1] = fibonaci(i-1)
        if d[i-2] == 0:
            d[i-2] = fibonaci(i-2)
        d[i] = d[i-1] + d[i-2]
        return d[i]

print(fibonaci(n))