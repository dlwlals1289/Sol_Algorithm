# 분수 찾기
import sys

X = int(input())

line = 1
a = 0 
b = 0 

while X > line:
    X -= line
    line += 1
   

if line % 2 == 0:
    a = X
    b = line + 1 - X

else:
    a = line + 1 - X
    b = X

print(f'{a}/{b}')