import math
from functools import reduce

def solution(arrayA, arrayB):
    answer = 0
    save = []
    
    gcd_A = reduce(math.gcd, arrayA)
    gcd_B = reduce(math.gcd, arrayB)
    
    for n in arrayB:
        if n % gcd_A == 0:
            gcd_A = 0
            break
            
    for n in arrayA:
        if n % gcd_B == 0:
            gcd_B = 0
            break
    return max(gcd_A, gcd_B)