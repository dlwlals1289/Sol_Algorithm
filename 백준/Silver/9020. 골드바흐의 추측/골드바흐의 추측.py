# 골든바흐의 추측
import sys
import math
input = sys.stdin.readline

def is_primenum(x):
    for i in range (2, int(math.sqrt(x) + 1)):
    	if x % i == 0:
        	return False
    return True
    
n = int(input())

for _ in range(n):
    num = int(input())
    
    a, b = num//2, num//2
    
    while a > 0:
        if is_primenum(a) and is_primenum(b):
            print(a, b)
            break
        
        a -= 1
        b += 1