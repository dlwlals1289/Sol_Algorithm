# 2xN 타일링
import sys

n = int(input())

d = [0 for i in range(1001)]
d[1] = 1
d[2] = 2
d[3] = 3

def square(i):
    if i == 1 :
        return 1
    elif i == 2 :
        return d[2]
    else:
        if(d[i-1] == 0):
            d[i-1] = square(i-1)
        if(d[i-2] == 0):
            d[i-2] = square(i-2)
        d[i] = d[i-1] + d[i-2]
        return d[i]

result = square(n)
result %= 10007
print(result)